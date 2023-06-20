from typing import Union, Dict

from src.Equipment import Equipment
from src.ExerciseType import ExerciseType
from src.MovementDirection import MovementDirection
from src.MovementType import MovementType
from src.MuscleContractions import MuscleContractions
from src.MuscleGroup import MuscleGroup
from src.MuscleGroupSecondary import MuscleGroupSecondary
from src.MuscleLength import MuscleLength


class CategoryGenerator:
    def __init__(self, classes: list):
        self.__category: Dict = {}
        self.classes = classes

    def with_equipment(self, value: str):
        self.__assert_value_in_class(value, Equipment)
        self.__category[Equipment.KEY] = value
        return self

    def with_exercise_type(self, value: str):
        self.__assert_value_in_class(value, ExerciseType)
        self.__category[ExerciseType.KEY] = value
        return self

    def with_movement_type(self, value: str):
        self.__assert_value_in_class(value, MovementType)
        self.__category[MovementType.KEY] = value
        return self

    def with_movement_direction(self, value: str):
        self.__assert_value_in_class(value, MovementDirection)
        self.__category[MovementDirection.KEY] = value
        return self

    def with_muscle_group(self, *values: str):
        return self.__append_muscle(values, MuscleGroup)

    def with_muscle_group_secondary(self, *values: str):
        return self.__append_muscle(values, MuscleGroupSecondary)

    def __append_muscle(self, values, cls=MuscleGroup):
        if not values:
            self.__category[cls.KEY] = ""
            return self

        for value in values:
            if not isinstance(value, list):
                value = [value]
            # assert all values in list are in cls
            for v in value:
                self.__assert_value_in_class(v, cls)
            self.__category[cls.KEY] = value
        return self

    def with_muscle_length(self, value: str):
        self.__assert_value_in_class(value, MuscleLength)
        self.__category[MuscleLength.KEY] = value
        return self

    def with_muscle_contractions(self, value: str):
        self.__assert_value_in_class(value, MuscleContractions)
        self.__category[MuscleContractions.KEY] = value
        return self

    def build(self) -> Dict[str, Union[str, list]]:
        for class_ in self.classes:
            if class_.KEY not in self.__category:
                raise Exception(f"Missing key {class_.KEY} in category")

        # Return the category dict after unset the __category
        category = self.__category
        self.__category = {}
        return category

    def __assert_value_in_class(self, value: str, class_) -> None:
        attributes = self.__get_attributes_of_class(class_)
        attribute = [attr for attr in attributes if getattr(class_, attr) == value]
        if not attribute:
            raise Exception(f"Value {value} not in {class_}")

    def __get_attributes_of_class(self, cls):
        return [attr for attr in dir(cls) if not attr.startswith('__') and not callable(getattr(cls, attr))]
