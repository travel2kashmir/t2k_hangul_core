from dataclasses import dataclass
from typing import List, Optional
from ..vocabulary import LocationPrecision, PropertyType

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json

from ..address import Address
from ..contact import Contact


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ListingBase(DataClassJsonMixin):
    property_id: str  # A unique identifier for the hotel.
    property_name: str  # name of the hotel
    property_country: str  # country that this listing is located in
    property_address: List[Address]  # full physical location of the hotel
    star_rating: int
    property_latitude: float
    property_longitude: float
    property_phone: List[Contact]


# END ListingDefaultsBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ListingDefaultsBase(DataClassJsonMixin):
    property_category: Optional[str] = PropertyType.DEFAULT  # business hotel, resort, motel
    property_brand: Optional[str] = None
    property_location_precision: Optional[int] = LocationPrecision.DEFAULT
    property_established_year: Optional[str] = None
    property_description_title: Optional[str] = None
    property_description_body: Optional[str] = None
    property_description_date: Optional[str] = None


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
