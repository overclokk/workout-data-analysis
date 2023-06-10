import unittest

from src.ExerciseType import ExerciseType
from src.MovementDirection import MovementDirection
from src.MovementType import MovementType
from src.MuscleGroup import MuscleGroup
from src.MuscleLength import MuscleLength
from src.CategoryGenerator import CategoryGenerator


def make_instance():
    return CategoryGenerator([
        ExerciseType,
        MovementType,
        MovementDirection,
        MuscleGroup,
        MuscleLength,
    ])


class TestCategoryGenerator(unittest.TestCase):

    def test_generator(self):
        generator = make_instance()
        # Test valid input
        result = generator.generate(
            ExerciseType.COMPOUND,
            MovementType.PUSH,
            MovementDirection.HORIZONTAL,
            MuscleGroup.CHEST,
            MuscleLength.NORMAL
        )
        self.assertEqual(result, {
            ExerciseType.KEY: ExerciseType.COMPOUND,
            MovementType.KEY: MovementType.PUSH,
            MovementDirection.KEY: MovementDirection.HORIZONTAL,
            MuscleGroup.KEY: MuscleGroup.CHEST,
            MuscleLength.KEY: MuscleLength.NORMAL,
        })

    def test_generator_with_list(self):
        generator = make_instance()
        # Test valid input
        result = generator.generate(
            ExerciseType.COMPOUND,
            MovementType.PUSH,
            MovementDirection.HORIZONTAL,
            [MuscleGroup.CHEST, MuscleGroup.TRICEPS],
            MuscleLength.NORMAL
        )
        self.assertEqual(result, {
            ExerciseType.KEY: ExerciseType.COMPOUND,
            MovementType.KEY: MovementType.PUSH,
            MovementDirection.KEY: MovementDirection.HORIZONTAL,
            MuscleGroup.KEY: [MuscleGroup.CHEST, MuscleGroup.TRICEPS],
            MuscleLength.KEY: MuscleLength.NORMAL,
        })

    def test_invalid_input(self):
        generator = make_instance()
        # Test invalid input
        result = generator.generate(
            ExerciseType.COMPOUND,
            MovementType.PUSH,
            MovementDirection.HORIZONTAL,
            MuscleGroup.CHEST,
            'invalid'
        )

        self.assertEqual(result, {
            ExerciseType.KEY: ExerciseType.COMPOUND,
            MovementType.KEY: MovementType.PUSH,
            MovementDirection.KEY: MovementDirection.HORIZONTAL,
            MuscleGroup.KEY: MuscleGroup.CHEST,
            MuscleLength.KEY: "",
        })


if __name__ == '__main__':
    unittest.main()
