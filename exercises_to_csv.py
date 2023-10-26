import csv

from src.Exercises import Exercises


def write_list_of_dicts_to_csv(data, filename):
    if not data:
        return

    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        headers = list(data[0].keys())
        writer.writerow(headers)
        for exercise_data in data:
            writer.writerow(generate_row_from_data(exercise_data, headers))


def generate_row_from_data(exercise_data, headers):
    return [format_value(exercise_data[header]) for header in headers]


def format_value(value):
    return ','.join(value) if isinstance(value, list) else value


write_list_of_dicts_to_csv(Exercises, 'data/exercises.csv')
