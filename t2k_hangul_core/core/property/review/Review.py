from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json
from typing import Optional
from ..vocabulary import ReviewType


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ReviewBase(DataClassJsonMixin):
    review_type: str = ReviewType.USER


# END ReviewBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ReviewDefaultsBase(DataClassJsonMixin):
    """
    webpage associated with the listing from the provider. Has the following child elements
    """
    review_link: Optional[str]
    review_title: Optional[str]
    review_author: Optional[str]  # title is a valid child element of <review> only if the review's type is editorial
    review_rating: Optional[str]
    review_body: Optional[str]
    review_date: Optional[str]
    service_date: Optional[str]  # <date> is only valid if type is user.
    review_date: Optional[str]


# END ReviewDefaultsBase


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Review(ReviewBase, ReviewDefaultsBase):
    pass

# END ReviewBase
