def fizz_buzz_generator(_user_input):
    while True:
        try:
            _user_input = int(_user_input)
            if _user_input < 1:
                continue
        except ValueError:
            continue
        break

    FizzBuzz = []

    for n in range(1, _user_input + 1):

        tmp = str(n)

        if (n % 3 == 0):
            tmp = "Fizz"
        if (n % 5 == 0 and tmp == "Fizz"):
            tmp += "Buzz"
        elif (n % 5 == 0):
            tmp = "Buzz"

        FizzBuzz.append(tmp)

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