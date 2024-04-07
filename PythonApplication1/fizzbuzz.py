class FizzBuzz:

        def getInput(num1):  
            try:
                return int(num1)
            except ValueError:
                print("num1 did not contain a number!")

        def fizzbuzz( i):
            if i % 15 == 0:
                return "FizzBuzz"
            elif i % 3 == 0:
                return "Fizz"
            elif i % 5 == 0:
                return "Buzz"
            else:
                return i

