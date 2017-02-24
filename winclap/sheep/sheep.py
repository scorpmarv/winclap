import os


def sheep_function(dataset):
    test_cases = 0
    for number in dataset:
        test_cases += 1
        iteration = 1
        found_numbers = set()
        max_number = number
        while len(found_numbers) != 10 and iteration < 201:
            max_number = str(number * iteration)
            for element in max_number:
                found_numbers.add(int(element))
            iteration += 1
        if len(found_numbers) == 10:
            print('Case #{}: {}'.format(test_cases, max_number))
        else:
            print('Case #{}: INSOMNIA'.format(test_cases))


def input_parameters(content):
    test_cases = 0
    dataset = []
    try:
        value = content.pop(0)
        if 0 < value < 101:
            test_cases = value
        else:
            raise ValueError
    except ValueError:
        print('Invalid number of cases')

    if test_cases == len(content):
        while test_cases > 0:
            try:
                current_number = content.pop(0)
                dataset.append(current_number)
                test_cases -= 1
            except ValueError:
                print('That is not a valid number')
        sheep_function(dataset)
    else:
        print('The number of elements do not match, expected: {}, given: {}'.format(test_cases, len(content)))


def open_file():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'c-input.in')
    with open(file_path) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    input_parameters(content)


if __name__ == "__main__":
    open_file()
