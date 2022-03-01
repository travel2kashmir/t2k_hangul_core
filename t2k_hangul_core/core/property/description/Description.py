from dataclasses import dataclass, field

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json
from typing import Optional


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class DescriptionBase(DataClassJsonMixin):
    description_body: str


# END DescriptionBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class DescriptionDefaultsBase(DataClassJsonMixin):
    """
    webpage associated with the listing from the provider. Has the following child elements """

    description_link: Optional[str]
    description_title: Optional[str]
    description_author: Optional[str]
    description_date: Optional[str]


# END DescriptionDefaultsBase


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Description(DescriptionDefaultsBase, DescriptionBase):
    pass

# END DescriptionBase
