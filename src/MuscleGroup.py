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
    ANTERIOR_DELTOID = 'anterior deltoid'
    LATERAL_DELTOID = 'lateral deltoid'
    POSTERIOR_DELTOID = 'posterior deltoid'

    # Legs
    QUADRICEPS = 'quadriceps'
    HAMSTRINGS = 'hamstrings'
    CALVES = 'calves'
    GLUTES = 'glutes'

    def key(self):
        return self.KEY
