import csv

csv_file_path_1 = "csv_files/r-m-c.csv"
csv_file_path_2 = "csv_files/rmc.csv"


def open_csv_file(csv_file_path) -> list[list[str]]:
    with open(csv_file_path, newline="") as csv_file:
        reader = csv.reader(csv_file)

        list_of_csv = list(reader)
        return list_of_csv


def filtered_set_of_csv(csv_file_1, csv_file_2) -> set[tuple]:
    third_set_of_csv: set[tuple] = set(tuple(row) for row in (csv_file_1 + csv_file_2))
    return third_set_of_csv


with open("csv_files/nedilko.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(filtered_set_of_csv(open_csv_file(csv_file_path_1), open_csv_file(csv_file_path_2)))

# print(unike_csv)
