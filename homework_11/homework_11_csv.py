import csv

with open("csv_files/r-m-c.csv", newline="", encoding="utf-8") as first_csv:
    reader = csv.reader(first_csv)

    first_list_of_csv: list = list(reader)

with open("csv_files/rmc.csv", newline="", encoding="utf-8") as second_csv:
    reader = csv.reader(second_csv)

    second_list_of_csv = list(reader)


def filtered_set_of_csv(csv_file_1, csv_file_2) -> set[tuple]:
    third_set_of_csv: set[tuple] = set(tuple(row) for row in (csv_file_1 + csv_file_2))
    return third_set_of_csv


with open("csv_files/nedilko.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(filtered_set_of_csv(first_list_of_csv, second_list_of_csv))
