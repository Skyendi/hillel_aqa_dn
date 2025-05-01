import csv

import pprint

with open("csv_files/r-m-c.csv", newline="") as first_csv:
    reader = csv.reader(first_csv)

    first_list_of_csv = list(reader)

    print(first_list_of_csv)

with open("csv_files/rmc.csv", newline="") as second_csv:
    reader = csv.reader(second_csv)

    second_list_of_csv = list(reader)

    print(second_list_of_csv)

third_list_of_csv: list[list] = first_list_of_csv + second_list_of_csv

unike_csv = []
set_of_csv = set()

for row in third_list_of_csv:
    row_tuple = tuple(row)
    if row_tuple not in set_of_csv:
        set_of_csv.add(row_tuple)
        unike_csv.append(row)

pprint.pprint(unike_csv)

with open("csv_files/nedilko.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(unike_csv)

# print(unike_csv)
