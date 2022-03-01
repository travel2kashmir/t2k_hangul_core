import uuid
from asyncio import AbstractEventLoop, get_event_loop
from copy import deepcopy
from typing import Any, Tuple

from rx.core.observable.observable import Observable
from rx.operators import distinct_until_changed, first, scan, to_future
from rx.subject.behaviorsubject import BehaviorSubject
from rx.subject.subject import Subject

from .types import StateType
from .utils import nested_set


def _reduce_state(state: StateType, payload: Any, *path: str):

    # By copying the given state and payload, we ensure that the store cannot be modified from outside
    target_state = nested_set(
        deepcopy(state),
        deepcopy(payload),
        *path
    )

    return target_state
# END _reduce_state


class Store():

    _default_state: StateType
    _done: Subject
    _loop: AbstractEventLoop
    _state: BehaviorSubject
    _updates: Subject

    def __init__(self, default_state: StateType = {}, loop: AbstractEventLoop = None):

        # Make a copy of the default state so that it cannot be modified from an outside source
        self._default_state = deepcopy(default_state)

        # Initialize the state observable with the default state
        self._state = BehaviorSubject(self._default_state)

        self._done = Subject()
        self._loop = loop or get_event_loop()
        self._updates = Subject()

        self._init_store()
    # END __init__

    def __del__(self):
        self._done.dispose()
        self._updates.dispose()
        self._state.dispose()
    # END __del__

    def delete(self, *path: str):
        return self._dispatch(None, *path)
    # END delete

    def reset(self):
        return self.set(self._default_state)
    # END reset

    def set(self, state: StateType):
        return self._dispatch(state)
    # END set

    def update(self, payload: Any, *path: str):
        return self._dispatch(payload, *path)
    # END update

    def _dispatch(self, payload: Any, *path: str):

        task_id = uuid.uuid4()
        event = (task_id, payload, path)

        completed = self._done.pipe(
            first(lambda id: id == task_id),
            to_future(self.loop.create_future)
        )

        self._updates.on_next(event)

        return completed
    # END _dispatch

    def _init_store(self):

        # Update the state for every update event
        self._updates.pipe(
            scan(self._reduce_event, self._default_state)
        ).subscribe(self._state)
    # END _init_store

    def _reduce_event(self, state: StateType, event: Tuple[uuid.UUID, Any, Tuple[str, ...]]):

        task_id, payload, path = event

        target_state = _reduce_state(state, payload, *path)

        self._done.on_next(task_id)

        return target_state
    # END _reduce_event

    @property
    def loop(self) -> AbstractEventLoop:
        return self._loop
    # END loop

    @property
    def state(self) -> Observable:
        return self._state.pipe(
            distinct_until_changed()
        )
    # END state

# END Store
