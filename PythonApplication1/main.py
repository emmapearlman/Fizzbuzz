from fizzbuzz import FizzBuzz


def main():
    print("Enter a number")
    val = input()
    num1 =FizzBuzz.getInput(val)

    print("Enter another number")
    val = input()
    num2 =FizzBuzz.getInput(val)

    for i in range(num1, num2):
        print(FizzBuzz.fizzbuzz(i))

  

if __name__ == '__main__':
    main()