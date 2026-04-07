from logic.suma import digitsSum

def run_test():
    assert digitsSum("999") == 27
    assert digitsSum("9184501") == 28
    assert digitsSum(12345) == 15
    print(" Suma de dígitos: Pasó")

if __name__ == "__main__": run_test()