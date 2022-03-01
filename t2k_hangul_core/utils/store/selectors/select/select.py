

from rx.core.observable.observable import Observable
from rx.operators import distinct_until_changed, map

from ...store import Store
from ...utils import nested_get


def select(store: Store, *path: str) -> Observable:

    # Emits the state at the given path every time it changes
    return store.state.pipe(
        map(lambda state: nested_get(state, *path)),
        distinct_until_changed()
    )
# END select
