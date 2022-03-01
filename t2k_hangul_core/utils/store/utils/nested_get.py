from functools import reduce

from ..types import StateType


def nested_get(state: StateType, *path: str):
    return reduce(
        lambda d, key: d.get(key) if d else None,
        path, state
    )
# END nested_get
