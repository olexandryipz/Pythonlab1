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

        element_count = len(results)
        print(f"Кількість елементів у списку: {element_count}")

        print("Парні елементи у списку:")
        for item in results:
            if isinstance(item, (int, float)) and item % 2 == 0:
                print(item)

    except ValueError:
        print("Помилка: введено нечислове значення. Будь ласка, введіть числа.")


if __name__ == "__main__":
    main()
