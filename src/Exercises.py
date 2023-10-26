from typing import Dict, List, Union

from src.Equipment import Equipment
from src.ExerciseType import ExerciseType
from src.MovementType import MovementType
from src.MovementDirection import MovementDirection
from src.MuscleContractions import MuscleContractions
from src.MuscleGroup import MuscleGroup
from src.MuscleGroupSecondary import MuscleGroupSecondary
from src.MuscleLength import MuscleLength
from src.ExerciseEntityGenerator import ExerciseEntityGenerator

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

generator = ExerciseEntityGenerator(category_generator_config)

Exercises: List[Dict[str, Union[str, List[str]]]] = [
    generator
        .for_name('Squat (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Bulgarian Split Squat')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Box Squat (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Pistol Squat')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Squat (Bodyweight)')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Clam shell')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.GLUTES)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ISOMETRIC)
        .build(),
    generator
        .for_name('Swiss Ball Hamstring Curl')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.HAMSTRINGS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Lat Pulldown (Cable)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Leg Extension (Machine)')
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Triceps Extension')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Bicep Curl (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Bench Press (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.FRONT_DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Bench Press - Close Grip (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.FRONT_DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Overhead Press (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.FRONT_DELTOID)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Lat Pulldown - Underhand (Band)')
        .with_equipment(Equipment.BANDS)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Front Squat (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS, MuscleGroupSecondary.GLUTES, MuscleGroupSecondary.CALVES)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Incline Bench Press (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.INCLINE)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.FRONT_DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Cable Crossover')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Deadlift (Barbell)')
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
    generator
        .for_name('Chest Fly (Band)')
        .with_equipment(Equipment.BANDS)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Lat Pulldown (Single Arm)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Bench Dip')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.CHEST, MuscleGroupSecondary.FRONT_DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Front Raise (Plate)')
        .with_equipment(Equipment.PLATE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.FRONT_DELTOID)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Bicep Curl (Cable)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Front Raise (Cable)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.FRONT_DELTOID)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Pendlay Row (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Plank')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CORE)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ISOMETRIC)
        .build(),
    generator
        .for_name('Romanian Deadlift (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.HAMSTRINGS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.BACK)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Inverted Row (Bodyweight)')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Incline Row (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.INCLINE)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Kneeling Pulldown (Band)')
        .with_equipment(Equipment.BANDS)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Incline Curl (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.INCLINE)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Seated Leg Press (Machine)')
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.GLUTES)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Incline Bench Press (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.INCLINE)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.FRONT_DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Lateral Raise (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.SIDE_DELTOID)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Side Plank')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CORE)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ISOMETRIC)
        .build(),
    generator
        .for_name('Triceps Extension (Cable)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Seated Row (Cable)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Pull Up')
        .with_equipment(Equipment.PULL_UP_BAR)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Push Up')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.FRONT_DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Floor Press (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.FRONT_DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Overhead Press (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.FRONT_DELTOID)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Bicep Curl (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('TricepsTRX')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Biceps TRX')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.SHORT_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Triceps Extension (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Ab Wheel')
        .with_equipment(Equipment.AB_WHEEL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CORE)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Hammer Curl (Cable)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Hammer Curl (Dumbbell)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Bent Over One Arm Row (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Romanian Deadlift (Dumbbell)')
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
    generator
        .for_name('Triceps Extension (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Chin Up')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Pull Up (Band)')
        .with_equipment(Equipment.BANDS)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Lunge (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Hip Thrust (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.GLUTES)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Leg Press')
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.GLUTES)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Chest Press (Machine)')
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.FRONT_DELTOID, MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Sumo Deadlift (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.GLUTES, MuscleGroup.QUADRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.BACK, MuscleGroupSecondary.HAMSTRINGS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Lying Leg Curl (Machine)')
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.HAMSTRINGS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Hip Thrust (Bodyweight)')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.GLUTES)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Shoulder Press (Machine)')
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.FRONT_DELTOID)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Skullcrusher (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Skullcrusher (Dumbbel)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.SHORT_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Push Press')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.FRONT_DELTOID)
        .with_muscle_group_secondary(MuscleGroupSecondary.TRICEPS, MuscleGroupSecondary.SIDE_DELTOID)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Bench Press (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.CHEST)
        .with_muscle_group_secondary(MuscleGroupSecondary.FRONT_DELTOID, MuscleGroupSecondary.TRICEPS)
        .with_muscle_length(MuscleLength.SHORT_LENGTH)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Lat Pulldown - Wide Grip (Cable)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Lat Pulldown (Machine)')
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.BICEPS)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Triceps Pushdown (Cable - Straight Bar)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Triceps KickBack')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.TRICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Glute Kickback (Machine)')
        .with_equipment(Equipment.MACHINE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.GLUTES)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Lunge (Bodyweight)')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Lunge (Barbell)')
        .with_equipment(Equipment.BARBELL)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.QUADRICEPS, MuscleGroup.GLUTES)
        .with_muscle_group_secondary(MuscleGroupSecondary.HAMSTRINGS)
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Reverse Fly (Cable)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.BACK)
        .with_muscle_group_secondary(MuscleGroupSecondary.REAR_DELTOID)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Lateral Raise (Cable)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.SIDE_DELTOID)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Handstand Push Up')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.COMPOUND)
        .with_movement_type(MovementType.PUSH)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.FRONT_DELTOID, MuscleGroup.SIDE_DELTOID, MuscleGroup.TRICEPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.CHEST, MuscleGroupSecondary.REAR_DELTOID)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.ECCENTRIC)
        .build(),
    generator
        .for_name('Reverse Crunch')
        .with_equipment(Equipment.BODY_WEIGHT)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.ABDOMINAL)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Face Pull (Cable)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.REAR_DELTOID, MuscleGroup.TRAPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.BACK)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Face Pull (Band)')
        .with_equipment(Equipment.CABLE)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.HORIZONTAL)
        .with_muscle_group(MuscleGroup.REAR_DELTOID, MuscleGroup.TRAPS)
        .with_muscle_group_secondary(MuscleGroupSecondary.BACK)
        .with_muscle_length(MuscleLength.LONG_LENGTH)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
    generator
        .for_name('Concentration Curl (Dumbbell)')
        .with_equipment(Equipment.DUMBBELL)
        .with_exercise_type(ExerciseType.ISOLATION)
        .with_movement_type(MovementType.PULL)
        .with_movement_direction(MovementDirection.VERTICAL)
        .with_muscle_group(MuscleGroup.BICEPS)
        .with_muscle_group_secondary()
        .with_muscle_length(MuscleLength.NORMAL)
        .with_muscle_contractions(MuscleContractions.CONCENTRIC)
        .build(),
]
