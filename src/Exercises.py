from typing import Dict

from src.Equipment import Equipment
from src.ExerciseType import ExerciseType
from src.MovementType import MovementType
from src.MovementDirection import MovementDirection
from src.MuscleContractions import MuscleContractions
from src.MuscleGroup import MuscleGroup
from src.MuscleGroupSecondary import MuscleGroupSecondary
from src.MuscleLength import MuscleLength
from src.CategoryGenerator import CategoryGenerator

category_generator_config = [
    Equipment,
    ExerciseType,
    MovementType,
    MovementDirection,
    MuscleGroup,
    MuscleGroupSecondary,
    MuscleLength,
    MuscleContractions,
]

generator = CategoryGenerator(category_generator_config)

Exercises: Dict[str, Dict[str, str]] = {
    'Bench Press (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Squat (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Bulgarian Split Squat': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Box Squat (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Pistol Squat': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Squat (Bodyweight)': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Lat Pulldown (Cable)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Leg Extension (Machine)': generator
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Triceps Extension': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Bicep Curl (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Bench Press - Close Grip (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Overhead Press (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.DELTOID)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Lat Pulldown - Underhand (Band)': generator
        .with_equipment(Equipment.BANDS)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Front Squat (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.GLUTES, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Incline Bench Press (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.INCLINE)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Cable Crossover': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Deadlift (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.HAMSTRINGS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(
            MuscleGroupSecondary.QUADRICEPS,
            MuscleGroupSecondary.BACK,
            MuscleGroupSecondary.CALVES
        )
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Chest Fly (Band)': generator
        .with_equipment(Equipment.BANDS)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Lat Pulldown (Single Arm)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Bench Dip': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.CHEST, MuscleGroupSecondary.DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Front Raise (Plate)': generator
        .with_equipment(Equipment.PLATE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.DELTOID)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Bicep Curl (Cable)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Front Raise (Cable)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.DELTOID)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Pendlay Row (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Plank': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CORE)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ISOMETRIC)
        .build(),
    'Romanian Deadlift (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.HAMSTRINGS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.BACK)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Inverted Row (Bodyweight)': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Incline Row (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.INCLINE)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Kneeling Pulldown (Band)': generator
        .with_equipment(Equipment.BANDS)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Incline Curl (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.INCLINE)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Seated Leg Press (Machine)': generator
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.GLUTES)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Incline Bench Press (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.INCLINE)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Lateral Raise (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.DELTOID)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Side Plank': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CORE)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ISOMETRIC)
        .build(),
    'Triceps Extension (Cable)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Seated Row (Cable)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Pull Up': generator
        .with_equipment(Equipment.PULL_UP_BAR)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Push Up': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Floor Press (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Overhead Press (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.DELTOID)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Bicep Curl (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'TricepsTRX': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Biceps TRX': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.SHORT_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Triceps Extension (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Ab Wheel': generator
        .with_equipment(Equipment.AB_WHEEL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CORE)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Hammer Curl (Cable)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Bent Over One Arm Row (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Romanian Deadlift (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.GLUTES)
        .with_muscle_group_secondary(
            MuscleGroupSecondary.HAMSTRINGS,
            MuscleGroupSecondary.QUADRICEPS,
            MuscleGroupSecondary.BACK
        )
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Triceps Extension (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Chin Up': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Pull Up (Band)': generator
        .with_equipment(Equipment.BANDS)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Lunge (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Hip Thrust (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.GLUTES)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Leg Press': generator
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.GLUTES)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Chest Press (Machine)': generator
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.DELTOID, MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Sumo Deadlift (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.GLUTES, MuscleGroup.QUADRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.BACK, MuscleGroupSecondary.HAMSTRINGS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Lying Leg Curl (Machine)': generator
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.HAMSTRINGS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Hip Thrust (Bodyweight)': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.GLUTES)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Shoulder Press (Machine)': generator
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.DELTOID)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Skullcrusher (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Push Press': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.DELTOID)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Bench Press (Dumbbell)': generator
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.DELTOID, MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.SHORT_LENGTH)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Lat Pulldown - Wide Grip (Cable)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Lat Pulldown (Machine)': generator
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Triceps Pushdown (Cable - Straight Bar)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Glute Kickback (Machine)': generator
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.GLUTES)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Lunge (Bodyweight)': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Lunge (Barbell)': generator
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Reverse Fly (Cable)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.DELTOID)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Lateral Raise (Cable)': generator
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.DELTOID)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    'Handstand Push Up': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.DELTOID, MuscleGroup.TRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.CHEST)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    'Reverse Crunch': generator
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.ABDOMINAL)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
}
