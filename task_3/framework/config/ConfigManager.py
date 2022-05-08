import csv
import json
from task_3.framework.errors.Errors import NoSuchElementError


class ConfigManager:
    PATH_TO_CONF_DATA = "task_3/framework/config/config_data.json"
    PATH_TO_TEST_DATA = "task_3/task/tests/test_data.json"
    PATH_TO_TEST_TABLE = "./task_3/task/tests/table.csv"

    def __init__(self):
        self.conf_path = ConfigManager.PATH_TO_CONF_DATA
        self.test_path = ConfigManager.PATH_TO_TEST_DATA
        self.table_path = ConfigManager.PATH_TO_TEST_TABLE

    def take_conf_param(self, param):
        with open(self.conf_path, "r") as conf_file:
            conf_data = json.load(conf_file)
            return conf_data[param]

    def take_test_param(self, param):
        with open(self.test_path, "r") as test_file:
            test_data = json.load(test_file)
            print(type(test_data))
        return test_data[param]

    def take_table_raw(self, user_num):
        with open(self.table_path, "r") as table_file:
            reader = csv.DictReader(table_file, delimiter=",")
            for line in enumerate(reader):
                # print(line)
                if line[1]["User №"] == user_num:
                    return line[1]
            raise NoSuchElementError(f"No User with number {user_num}.")
