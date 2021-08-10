from enum import Enum
from typing import List, Tuple


class DjangoChoicesEnum(Enum):
    @classmethod
    def to_choices_list(cls) -> List[Tuple[str, str]]:
        return [(member.value, member.name) for member in cls.__members__.values()]
