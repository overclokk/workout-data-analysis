class MuscleGroup:
    KEY = 'Muscle_Group'
    # Muscle groups (https://www.bodybuilding.com/exercises/muscle/biceps)

    # Front
    CHEST = 'chest'

    # Back
    BACK = 'back'
    TRAPS = 'traps'

    # Side
    NECK = 'neck'
    ABS = 'abs'
    CORE = 'core'
    ABDOMINAL = 'abdominal'
    OBLIQUES = 'obliques'

    # Arms
    BICEPS = 'biceps'
    TRICEPS = 'triceps'
    FOREARMS = 'forearms'
    DELTOID = 'deltoid'
    FRONT_DELTOID = 'front deltoid'
    SIDE_DELTOID = 'side deltoid'
    REAR_DELTOID = 'rear deltoid'

    # Legs
    QUADRICEPS = 'quadriceps'
    HAMSTRINGS = 'hamstrings'
    CALVES = 'calves'
    GLUTES = 'glutes'

    def key(self):
        return self.KEY
