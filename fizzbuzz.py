def fizz_buzz_generator(user_input):
    while True:
        try:
            user_input = int(user_input)
            if user_input < 1:
                continue
        except ValueError:
            continue
        break

    FizzBuzz = []

    n = 1

    while n <= user_input:
        x = str(n)
        Fizz = (n % 3 == 0)
        Buzz = (n % 5 == 0) 

        if Fizz:
            x = "Fizz"
        if Buzz and x == "Fizz":
            x += "Buzz"
        elif Buzz:
            x = "Buzz"

        FizzBuzz.append(x)
        n += 1

    print(FizzBuzz)

fizz_buzz_generator(input("Voer één geheel getal in wat groter is dan 0 (e.g. 15): "))

while True:
    try:
        user_input = input("Wilt u nog een keer input geven voor de FizzBuzz generator? (Y/N): ").upper()
    except ValueError:
        continue

    if user_input == 'Y':
        fizz_buzz_generator(input("Voer één geheel getal in wat groter is dan 0: "))
    elif user_input == 'N':
        break