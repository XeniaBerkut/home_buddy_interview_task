import json
import os
import time


def make_email_unique(email: str) -> str:
    first_email_part = email[:email.index('@')]
    second_email_part = email.replace(first_email_part, '')
    return first_email_part + str(time.time_ns() % 1000000) + second_email_part


def create_unique_phone_number(code) -> str:
    time_str = str(time.time_ns())
    random_number = time_str[-7:]
    return code + random_number


def get_test_data_from_json(test_data_file_name: str) -> dict:
    json_path = os.path.join(test_data_file_name)
    with open(json_path, "r") as json_file:
        test_data = json.load(json_file)
    return test_data


def expected_thanks_text(name):
    first_name = name[:name.index(' ')]
    expected_text = 'Thank you ' + first_name + ', your contractor QA company will call soon!'
    return expected_text
