def main():
    try:
        name = input("Введіть ваше прізвище та ім’я: ").strip()

        if not name or any(char.isdigit() for char in name):
            raise ValueError("Ім'я та прізвище мають містити лише букви.")

        print("\nВиконавець лабораторної роботи:")
        print(f"Прізвище та ім’я: {name}")

        print("\nВисновки:")
        print("Я ознайомився з алгоритмами послідовної (лінійної) структури,")
        print("застосував інтегроване середовище розробки Python (IDLE),")
        print("а також засвоїв основи введення та виведення даних у Python.")

    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

if __name__ == "__main__":
    main()
