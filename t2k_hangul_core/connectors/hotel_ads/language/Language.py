from dataclasses import dataclass, field

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json
from typing import Optional


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class LanguageBase(DataClassJsonMixin):
    pass


# END LanguageBase

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class LanguageDefaultsBase(DataClassJsonMixin):
    """
    The language in which your feed is written. Set the value of this element to a two-letter language code. For example, "en" for English
    """
    language: str = field(default='english')


# END LanguageDefaultsBase


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Language(LanguageDefaultsBase, LanguageBase):
    pass

# END LanguageBase
