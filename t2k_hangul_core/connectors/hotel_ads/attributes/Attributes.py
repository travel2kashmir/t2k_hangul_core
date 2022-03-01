from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json
from typing import Optional, List

from ..vocabulary import ClientAttribute


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class AttributesBase(DataClassJsonMixin):
    pass


# END AttributesBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class AttributesDefaultsBase(DataClassJsonMixin):
    website: Optional[str]
    client_attr: Optional[List[ClientAttribute]]

# END AttributesDefaultsBase


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Attributes(AttributesDefaultsBase, AttributesBase):
    """
    can be used to describe property amenities and to classify ratings and reviews of the property
    """
    pass

# END AttributesBase
