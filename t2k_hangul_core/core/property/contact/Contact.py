from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin, LetterCase, dataclass_json


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class Contact(DataClassJsonMixin):
    type: str
    value: str

# END Phone
