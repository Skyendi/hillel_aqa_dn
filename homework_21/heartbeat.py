from datetime import datetime, time
from homework_21.file_logger import logger


def report_filter_with_key(key, report_file):
    filtered_report = []
    with open(report_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if key in line:
                filtered_report.append(line)
    return filtered_report


def find_time_stamp(report):
    key = "Timestamp "
    list_of_time = []
    for line in report:
        idx = line.find(key)
        time_str = line[idx + len(key):idx + len(key) + 8]
        # print(time_str)
        time_data = datetime.strptime(time_str, "%H:%M:%S")
        list_of_time.append(time_data)
    return list_of_time


def count_time_differences(time_report):
    time_differences = []
    for i in range(len(time_report) - 1):
        differences = time_report[i] - time_report[i + 1]
        time_differences.append(differences)
    return time_differences


def report_logger(time_diff):
    for diff in time_diff:
        if diff.total_seconds() == 32:
            logger.warning("WARNING")
        if diff.total_seconds() >= 33:
            logger.error("ERROR")


if __name__ == "__main__":
    report_filter = report_filter_with_key(key="Key TSTFEED0300|7E3E|0400", report_file="heartbeat_report.txt")
    filtered_report = find_time_stamp(report_filter)
    time_differences = count_time_differences(filtered_report)
    report_logger(time_differences)
