from functools import reduce
from typing import Any

from ..types import StateType


def nested_set(state: StateType, payload: Any, *path: str):

    if len(path) == 0:
        return payload
    # END IF

    *branches, leaf = path

    if len(branches) == 0:
        target_branch = state
    else:
        target_branch = reduce(
            lambda branch, parent: branch.setdefault(parent, {}),
            branches, state
        )
    # END IF

    target_branch[leaf] = payload

    return state
# END nested_set
