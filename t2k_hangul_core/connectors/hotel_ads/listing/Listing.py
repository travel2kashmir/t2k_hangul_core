from dataclasses import dataclass
from typing import List, Optional
from ..vocabulary import PropertyType
from ..content import Content

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json

from ..address import Address
from ..contact import Contact

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ListingBase(DataClassJsonMixin):
    id: str  # A unique identifier for the hotel.
    name: str  # name of the hotel
    address: List[Address]  # full physical location of the hotel
    country: str  # country that this listing is located in
    star_rating: int
    latitude: float
    longitude: float
    phone: List[Contact]


# END ListingDefaultsBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ListingDefaultsBase(DataClassJsonMixin):
    content: Optional[Content] = None
    category: Optional[str] = PropertyType.DEFAULT  # business hotel, resort, motel


# END ListingBase


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Listing(ListingDefaultsBase, ListingBase):
    """
    One or more entries that describe each hotel in the feed.
    Note that each hotel in the list must have an ID that is unique to your site,
     and that this ID should never be re-used.
    """
    pass
# END Listing



