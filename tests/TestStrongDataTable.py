import unittest

from src.StrongDataTable import StrongDataTable


class TestStrongDataTable(unittest.TestCase):
    def setUp(self):
        self.exercises = {
            'Bench Press (Barbell)': {
                'equipment': 'barbell',
                'exercise_type': 'compound',
                'movement_type': 'push',
                'movement_direction': 'horizontal',
                'muscle_group': ['chest', 'triceps'],
                'muscle_length': 'fisiological'
            },
            # Add more exercises as needed
        }
        self.csv_file_path = 'fixtures/fake_strong.csv'  # replace with your test csv file path
        self.data_table = StrongDataTable(self.csv_file_path, self.exercises)

    def test_build(self):
        df = self.data_table.build()
        # Now you can assert conditions on df
        # For example, you can check if the DataFrame has the expected columns
        # expected_columns = ['Date', 'Workout Name', 'Exercise Name', 'Set Order', 'Weight',
        #                     'Weight Unit', 'Reps', 'RPE', 'Distance', 'Distance Unit', 'Seconds',
        #                     'Notes', 'Workout Notes', 'Workout Duration', 'Time', 'Lifted',
        #                     'Reps with load', 'Reps BW', 'Weekday', 'Month', 'Year', 'Week_Number',
        #                     'Year-Week_Number', 'Muscle_Length', 'Muscle_Group', 'Equipment',
        #                     'Exercise_Type', 'Movement_Type', 'Movement_Direction']
        # expected_columns = ['Date', 'Workout Name', 'Exercise Name', 'Set Order', 'Weight', 'Weight Unit', 'Reps', 'RPE', 'Distance', 'Distance Unit', 'Seconds', 'Notes', 'Workout Notes', 'Workout Duration', 'Time', 'Lifted', 'Reps with load', 'Reps BW', 'Weekday', 'Month', 'Year', 'Week_Number', 'Year-Week_Number', 'movement_direction', 'equipment', 'movement_type', 'muscle_group', 'muscle_length', 'exercise_type']
        # self.assertListEqual(list(df.columns), expected_columns)
        # print(list(df.columns))

        # You can also check if the DataFrame has the expected number of rows
        # Replace 'expected_number_of_rows' with the actual expected number
        expected_number_of_rows = 20
        self.assertEqual(len(df), expected_number_of_rows)


if __name__ == '__main__':
    unittest.main()
