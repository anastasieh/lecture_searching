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

def binary_search(numbers, hledane_cislo):
    levy_okraj = 0
    pravy_okraj = len(numbers) - 1
    while levy_okraj <= pravy_okraj:
        stred = round((levy_okraj + pravy_okraj) / 2)
        if numbers[stred] == hledane_cislo:
            return stred
        elif numbers[stred] < hledane_cislo:
            levy_okraj = stred +1
        else:
            pravy_okraj = stred -1
    return None
    # print(levy_okraj, pravy_okraj, stred)












def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    vysledek = linear_search(sequential_data, 14)
    sequential_data2 = read_data("sequential.json", "ordered_numbers")
    vysledek2 = binary_search(sequential_data2, 13)
    pass
    print(sequential_data2)
    print(vysledek)
    print(vysledek2)
if __name__ == '__main__':
    main()