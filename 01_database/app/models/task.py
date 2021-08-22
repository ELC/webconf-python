from typing import NamedTuple, Optional


class Task(NamedTuple):
    id: int
    text: Optional[str] = None
    day: Optional[str] = None
    reminder: Optional[bool] = None


##############################################################################


# Alternative 1

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class TaskDataclass:
    id: int
    text: Optional[str] = None
    day: Optional[str] = None
    reminder: Optional[bool] = None


###############################################################################


# Alternative 2

from typing import Optional


class TaskPure:
    def __init__(
        self,
        id_: int,
        text: Optional[str] = None,
        day: Optional[str] = None,
        reminder: Optional[bool] = None,
    ):
        self.id: int = id_
        self.text: Optional[str] = text
        self.day: Optional[str] = day
        self.reminder: Optional[bool] = reminder
