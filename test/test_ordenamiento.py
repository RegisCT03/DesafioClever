from logic.ordenamiento import integerSort

def run_test():
    input_array = [5, -2, 10, 0, 3, -7]
    result = integerSort(input_array)
    assert result == [-7, -2, 0, 3, 5, 10]
    assert input_array == [5, -2, 10, 0, 3, -7]
    print("Ordenamiento: Pasó")

if __name__ == "__main__":
    run_test()