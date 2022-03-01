from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json
from typing import Optional
from ..vocabulary import ReviewType


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ReviewBase(DataClassJsonMixin):
    type: str = ReviewType.USER


# END ReviewBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ReviewDefaultsBase(DataClassJsonMixin):
    """
    webpage associated with the listing from the provider. Has the following child elements
    """
    link: Optional[str]
    title: Optional[str]  # title is a valid child element of <review> only if the review's type is editorial
    author: Optional[str]
    rating: Optional[str]
    body: Optional[str]
    date: Optional[str]
    servicedate: Optional[str]  # <date> is only valid if type is user.

# END ReviewDefaultsBase


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Review(ReviewBase, ReviewDefaultsBase):
    pass

# END ReviewBase
