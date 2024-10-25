def main():
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        results = []

        results.append(num1 + num2)
        results.append(num1 - num2)
        results.append(num1 * num2)

        if num2 != 0:
            results.append(num1 / num2)
            results.append(num1 // num2)
            results.append(num1 % num2)
        else:
            results.append("Ділення на нуль неможливе")
            results.append("Цілочисленне ділення на нуль неможливе")
            results.append("Остача від ділення на нуль неможлива")

        results.append(num1 ** num2)

        print("Результати:")
        for res in results:
            print(res)

    except ValueError:
        print("Помилка: введено нечислове значення. Будь ласка, введіть числа.")

if __name__ == "__main__":
    main()
