from dataclasses import dataclass
from enum import Enum
from functools import wraps
from typing import Any, Generic, Optional, TypeVar
from uuid import UUID, uuid4

from typing_extensions import Protocol

T = TypeVar('T')


class OutcomeStatus(Enum):
    ERROR = 'ERROR'
    SUCCESS = 'SUCCESS'
# END OutcomeStatus


@dataclass(frozen=True)
class Outcome(Generic[T]):

    error: BaseException = None
    sequence_id: UUID = None
    status: OutcomeStatus = OutcomeStatus.SUCCESS
    value: Optional[T] = None

    def raise_for_error(self):
        if self.error is not None:
            raise self.error
        # END IF
    # END raise_if_error

# END Outcome


PipelineTask = Any
Bindable = Any


def bind(func: Bindable) -> PipelineTask:

    @wraps(func)
    def wrapped(*args, **kwargs):

        outcome = None

        try:
            result = func(*args, **kwargs)
            outcome = Outcome(value=result)
        except Exception as e:
            outcome = Outcome(
                error=e,
                status=OutcomeStatus.ERROR
            )
        # END TRY

        return outcome
    # END wrapped

    return wrapped
# END bind
