from enum import Enum
from typing import Any, Union, Dict

from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json


class ClientAttributeName(Enum):
    AIR_CONDITIONED = "air_conditioned"
    ALL_INCLUSIVE_AVAILABLE = "all_inclusive_available"
    ALTERNATE_HOTEL_ID = "alternate_hotel_id"
    CHILD_FRIENDLY = "child_friendly"
    SWIMMING_POOL_TYPE = "swimming_pool_type"


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ClientAttribute(DataClassJsonMixin):
    ClientAttribute: Dict[ClientAttributeName, Union[Any]]

# END ClientAttribute
