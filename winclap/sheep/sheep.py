
def sheep_function():
    test_cases = 0
    dataset = []
    while test_cases == 0:
        try:
            value = int(input('Please select how many test cases you want to run (remember min=1, max=100): '))
            if 0 < value < 101:
                test_cases = value
            else:
                raise ValueError
        except ValueError:
            print('That is not a valid number')

    while test_cases > 0:
        try:
            current_number = int(input('Please insert a number: '))
            dataset.append(current_number)
            test_cases -= 1
        except ValueError:
            print('That is not a valid number')

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


if __name__ == "__main__":
    sheep_function()
