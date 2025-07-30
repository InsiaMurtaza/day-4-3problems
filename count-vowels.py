def count_vowels(word:str):
    word_lower = word.lower()
    vowels = "aeiou"
    i= 0
    for alpha in word_lower:
        if alpha in vowels:
            i+=1
    return i
        
def main():
    user_input = input("Enter a word: ")
    count_vowels_in_word = count_vowels(user_input)
    print(count_vowels_in_word)

if __name__ == "__main__":
    main()


    
    

        


