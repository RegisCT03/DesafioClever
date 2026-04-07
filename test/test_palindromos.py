from logic.palindromos import isPalindrome

def run_test():
    assert isPalindrome("aabaa") is True
    assert isPalindrome("abac") is False
    assert isPalindrome("salas") is True
    print("Palíndromos: Pasó")

if __name__ == "__main__":
    run_test()