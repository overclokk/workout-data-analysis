from typing import Protocol


class Category(Protocol):

    def key(self) -> str:
        ...
