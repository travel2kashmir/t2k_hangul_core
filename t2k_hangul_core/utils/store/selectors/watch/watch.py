from enum import Enum, auto

from rx.core.observable.observable import Observable
from rx.operators import filter, map, pairwise

from ...store import Store
from ..select import select


class WatchType(Enum):
    DICT = auto()
    LIST = auto()
# END WatchType


def watch(store: Store, *path: str, watch_type: WatchType = WatchType.LIST) -> Observable:

    def reduce(state):
        if state is None:
            return {}
        # END IF

        reducers = {
            WatchType.DICT: dict.items,
            WatchType.LIST: set
        }

        reducer = reducers.get(watch_type, reducers[WatchType.LIST])

        target_state = reducer(state)

        return target_state
    # END reduce_dict

    return select(store, *path).pipe(
        map(reduce),
        pairwise(),
        map(lambda pair: pair[1] - pair[0]),
        filter(lambda diff: len(diff) > 0),
    )
# END watch
