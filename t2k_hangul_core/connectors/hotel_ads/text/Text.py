from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json
from typing import Optional, List


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class TextBase(DataClassJsonMixin):
    type: str = "description"


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class TextDefaultsBase(DataClassJsonMixin):
    link: str
    title: str
    body: str
    date: str


# END TextDefaultsBase


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Text(TextBase, TextDefaultsBase):
    pass

# END Text
