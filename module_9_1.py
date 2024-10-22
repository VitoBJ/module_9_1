
def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:

        results[func.__name__] = func(int_list)

    return results


def sum_list(numbers):
    return sum(numbers)

def max_list(numbers):
    return max(numbers)

def min_list(numbers):
    return min(numbers)

def average_list(numbers):
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    my_numbers = [10, 20, 30, 40, 50]
    results = apply_all_func(my_numbers, sum_list, max_list, min_list, average_list)
    print(results)
