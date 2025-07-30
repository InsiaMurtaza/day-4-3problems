def reverse_string(word:str):
    reverse_word = word[::-1]
    return reverse_word

def main():
    user_input = input("Enter a word: ")
    str_rev = reverse_string(user_input)
    print(str_rev)

if __name__ == "__main__":
    main()