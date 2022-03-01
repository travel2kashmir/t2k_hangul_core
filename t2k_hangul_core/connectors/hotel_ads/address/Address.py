from dataclasses import dataclass
from typing import Optional
from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class AddressBase(DataClassJsonMixin):
    addr1: str
    city: str
    province: str
    postal_code: str


# END AddressBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class AddressDefaultsBase(DataClassJsonMixin):
    addr2: Optional[str] = None
    addr3: Optional[str] = None


# END AddressDefaultsBase


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Address(AddressDefaultsBase, AddressBase):
    """
    The full physical location of the hotel.
    """

    def to_simple_address_format(self) -> str:
        """
        Simple address format as required by Google.
        :return: str
        """
        # Filter None values from Address
        addr_dict = dict(
            filter(lambda x: x[1],
                   self.to_dict().items()
                   )
        )

        return ", ".join(v for k, v in addr_dict.items())

# END AddressBase
