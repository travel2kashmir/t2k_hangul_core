from asyncio import Future

from rx.operators import Predicate, first, to_future

from ...store import Store
from ..select import select


def get(store: Store, *path: str, predicate: Predicate = None) -> Future:
    # Return the first value that fulfils the given predicate
    return select(store, *path).pipe(
        first(predicate),
        to_future(store.loop.create_future)
    )
# END get
