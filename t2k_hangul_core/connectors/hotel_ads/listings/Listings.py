from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json

from ..listing import Listing
from ..language import Language


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ListingsDefaultsBase(DataClassJsonMixin):
    language: Language
    listing: Listing


# END ListingsDefaultsBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class ListingsBase(DataClassJsonMixin):
    pass


# END ListingsBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Listings(DataClassJsonMixin):
    pass

# END Listings
