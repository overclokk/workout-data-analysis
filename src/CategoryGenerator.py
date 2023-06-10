from typing import Union, Dict


class CategoryGenerator:
    def __init__(self, classes: list):
        self.classes = classes

    def generate(self, *args: Union[str, list]) -> Dict[str, Union[str, list]]:
        category = {class_.KEY: "" for class_ in self.classes}

        for value in args:
            self._update_category(category, value)

        return category

    def _update_category(self, category: Dict[str, Union[str, list]], value: Union[str, list]) -> None:
        if not isinstance(value, list):
            self._update_category_with_value(category, value)

        new_value: list[str] = []
        key = ""
        for v in value:
            for class_ in self.classes:
                if v in class_.__dict__.values():
                    key = class_().key()
                    new_value.append(v)
                    break

        if key in category:
            category[key] = new_value

    def _update_category_with_value(self, category: Dict[str, Union[str, list]], value: str) -> None:
        for class_ in self.classes:
            if value in class_.__dict__.values():
                key = class_().key()
                category[key] = value
                return
