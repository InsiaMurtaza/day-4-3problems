def sum_of_digits(num:int):
    if num.is_integer:
        num_str = str(num)
        if len(num_str) > 1:
            sum=0
            for digit_char in num_str:
                sum += int(digit_char)
    return sum

def main():
    while True:
        try:
            user_input = int(input("Enter a number: "))
            summing_digits = sum_of_digits(user_input)
            print(summing_digits)
            break
        except ValueError:
            print("Oops! You did not enter number..")
    
       
if __name__ == "__main__":
    main()