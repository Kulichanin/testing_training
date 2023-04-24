def plus(num_1:int, num_2:int) -> int:
    return num_1 + num_2

def minus(num_1:int, num_2:int) -> int:
    return num_1 - num_2

def multiply(num_1:int, num_2:int) -> int:
    return num_1 * num_2

def divide(num_1:int, num_2:int) -> float:
    return num_1 / num_2

def main():
    #TODO: Подумать над выводом операции не через логику а через словарь

    try:
        num_1 = int(input('Напишите первое число: '))
        sign = int(input('Введите цифру от 1 до 4 где: 1 = +, 2 = -, 3 = *, 4 = : '))
        num_2 = int(input('Напишите второе число: '))
    except ValueError:
        print('Ввидите целое число')


if __name__ == "__main__":
    main()
