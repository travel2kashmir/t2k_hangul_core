from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json
from typing import Optional, List

from ..review import Review


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ContentBase(DataClassJsonMixin):
    pass


# END ContentBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ContentDefaultsBase(DataClassJsonMixin):
    """
    Adds information about a listing, such as ratings and reviews, amenities, and other details.
    The <content> element is optional.
    Within <content>, all child elements are optional."""

    review: Optional[List[Review]]


# END ContentDefaultsBase


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Content(ContentDefaultsBase, ContentBase):
    pass

# END ContentBase
