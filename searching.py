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

def linear_search(field, hledane_cislo):
    positions = []
    count = 0
    for i in range(len(field)):
        if field[i] == hledane_cislo:
            positions.append(i)
            count += 1
    slovnik = {"positions":  positions, "count": count}
    return  slovnik



def main():
    sequential_data = read_data("sequential.json", "ordered_numbers")
    vysledek = linear_search(sequential_data, 14)
    pass
    print(sequential_data)
    print(vysledek)
if __name__ == '__main__':
    main()