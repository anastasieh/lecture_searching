import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        if field not in data:
            return None
        else:
            return data[field]



def main():
    sequential_data = read_data("sequential.json", "ordered_numbers")
    pass
    print(sequential_data)

if __name__ == '__main__':
    main()