def fizzbuzz(fizz=3,buzz=5,duration=100):
    for i in range(1,duration+1):
        if i % fizz == 0:
            if i % buzz == 0:
                print("Fizz Buzz")
            else:
                print("Fizz")
        elif i % buzz == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()