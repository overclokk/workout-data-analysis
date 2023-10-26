import unittest

from src.Equipment import Equipment
from src.ExerciseType import ExerciseType
from src.Exercises import category_generator_config
from src.MovementDirection import MovementDirection
from src.MovementType import MovementType
from src.MuscleContractions import MuscleContractions
from src.MuscleGroup import MuscleGroup
from src.MuscleGroupSecondary import MuscleGroupSecondary
from src.MuscleLength import MuscleLength
from src.ExerciseEntityGenerator import ExerciseEntityGenerator


def make_instance():
    return ExerciseEntityGenerator(category_generator_config)


class TestExerciseEntityGenerator(unittest.TestCase):

    def test_build(self):
        sut = make_instance()
        actual = sut \
            .with_equipment(Equipment.BARBELL) \
            .with_exercise_type(ExerciseType.COMPOUND) \
            .with_movement_type(MovementType.PUSH) \
            .with_movement_direction(MovementDirection.HORIZONTAL) \
            .with_muscle_group(MuscleGroup.CHEST) \
            .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS) \
            .with_muscle_length(MuscleLength.NORMAL) \
            .with_muscle_contractions(MuscleContractions.ECCENTRIC) \
            .build()
        expected = {
            Equipment.KEY: Equipment.BARBELL,
            ExerciseType.KEY: ExerciseType.COMPOUND,
            MovementType.KEY: MovementType.PUSH,
            MovementDirection.KEY: MovementDirection.HORIZONTAL,
            MuscleGroup.KEY: [MuscleGroup.CHEST],
            MuscleGroupSecondary.KEY: [MuscleGroupSecondary.TRICEPS],
            MuscleLength.KEY: MuscleLength.NORMAL,
            MuscleContractions.KEY: MuscleContractions.ECCENTRIC,
        }
        self.assertEqual(actual, expected)

    def test_generator_with_list_for_secondary(self):
        sut = make_instance()
        actual = sut\
            .with_equipment(Equipment.BARBELL)\
            .with_exercise_type(ExerciseType.COMPOUND)\
            .with_movement_type(MovementType.PUSH)\
            .with_movement_direction(MovementDirection.HORIZONTAL)\
            .with_muscle_group(MuscleGroup.CHEST, MuscleGroup.DELTOID)\
            .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS)\
            .with_muscle_length(MuscleLength.NORMAL)\
            .with_muscle_contractions(MuscleContractions.ECCENTRIC)\
            .build()
        expected = {
            Equipment.KEY: Equipment.BARBELL,
            ExerciseType.KEY: ExerciseType.COMPOUND,
            MovementType.KEY: MovementType.PUSH,
            MovementDirection.KEY: MovementDirection.HORIZONTAL,
            MuscleGroup.KEY: [MuscleGroup.CHEST, MuscleGroup.DELTOID],
            MuscleGroupSecondary.KEY: [MuscleGroupSecondary.TRICEPS],
            MuscleLength.KEY: MuscleLength.NORMAL,
            MuscleContractions.KEY: MuscleContractions.ECCENTRIC,
        }
        self.assertEqual(actual, expected)

    def test_generator_with_empty_secondary(self):
        sut = make_instance()
        actual = sut\
            .with_equipment(Equipment.BARBELL)\
            .with_exercise_type(ExerciseType.COMPOUND)\
            .with_movement_type(MovementType.PUSH)\
            .with_movement_direction(MovementDirection.HORIZONTAL)\
            .with_muscle_group(MuscleGroup.CHEST)\
            .with_muscle_group_secondary()\
            .with_muscle_length(MuscleLength.NORMAL)\
            .with_muscle_contractions(MuscleContractions.ECCENTRIC)\
            .build()
        expected = {
            Equipment.KEY: Equipment.BARBELL,
            ExerciseType.KEY: ExerciseType.COMPOUND,
            MovementType.KEY: MovementType.PUSH,
            MovementDirection.KEY: MovementDirection.HORIZONTAL,
            MuscleGroup.KEY: [MuscleGroup.CHEST],
            MuscleGroupSecondary.KEY: "",
            MuscleLength.KEY: MuscleLength.NORMAL,
            MuscleContractions.KEY: MuscleContractions.ECCENTRIC,
        }
        self.assertEqual(actual, expected)

    def test_invalid_input(self):
        sut = make_instance()
        methods = [getattr(sut, method_name) for method_name in dir(sut) if method_name.startswith('with_')]
        for method in methods:
            with self.assertRaises(Exception):
                method('invalid')


if __name__ == '__main__':
    unittest.main()
