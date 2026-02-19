def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join(char for char in s if char not in vowels)


if __name__ == "__main__":
    s = input("Enter a string: ")
    print(remove_vowels(s))
