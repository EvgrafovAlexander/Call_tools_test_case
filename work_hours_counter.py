# stdlib
import argparse
import logging
from collections import defaultdict
from pathlib import Path


def print_working_hours_stat(path_to_file: Path) -> None:
    """
    Выводит статистику по каждому работнику + сумму выполненных часов

    :param path_to_file: путь к файлу
    :return: None
    """
    hours_counter = defaultdict(list)
    with open(path_to_file, encoding='utf-8') as f:
        for line in f:
            try:
                name, work_hours = line.rsplit(" ", 1)
                hours_counter[name].append(int(work_hours))
            except ValueError as e:
                logging.error("Запись '{}' не распознана, описание ошибки: {}".format(line, e))

        for name, list_of_hours in hours_counter.items():
            print("{}: {}; sum: {}".format(name, ", ".join(map(str, list_of_hours)), sum(list_of_hours)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path_to_file", type=str, help="Path to file with data, format: 'name number_of_hours'")
    args = parser.parse_args()

    path_to_file = Path(args.path_to_file)
    print_working_hours_stat(path_to_file)
