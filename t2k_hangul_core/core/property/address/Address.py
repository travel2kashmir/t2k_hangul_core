from dataclasses import dataclass
from typing import Optional
from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json

# Google API
from ....connectors.hotel_ads import Address as GoogleAddress


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class AddressBase(DataClassJsonMixin):
    property_addr1: str
    property_city: str
    property_province: str
    property_postal_code: str


# END AddressBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class AddressDefaultsBase(DataClassJsonMixin):
    property_addr2: Optional[str] = None
    property_addr3: Optional[str] = None
    property_street_address: Optional[str] = None
    property_landmark: Optional[str] = None


# END AddressDefaultsBase


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Address(AddressDefaultsBase, AddressBase):
    """
    The full physical location .
    """

    @property
    def to_google(self) -> GoogleAddress:
        """
        converts Address structure to Google Address requirement
        :return: GoogleAddress
        """
        return GoogleAddress.from_dict({
            "addr1": self.property_addr1,
            "addr2": self.property_addr2,
            "addr3": self.property_addr3,
            "city": self.property_city,
            "province": self.property_province,
            "postal_code": self.property_postal_code
        })

    # END AddressBase
