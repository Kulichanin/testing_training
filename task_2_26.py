def plus(num_1:int, num_2:int) -> int:
    return num_1 + num_2

def minus(num_1:int, num_2:int) -> int:
    return num_1 - num_2

def multiply(num_1:int, num_2:int) -> int:
    return num_1 * num_2

def divide(num_1:int, num_2:int):
    try:
        return int(num_1 / num_2)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')

def main():
    try:
        num_one = int(input('Напишите первое число: '))
        sign = input('Введите арифметический знак +, -, *, /: ')
        num_two = int(input('Напишите второе число: '))
    except ValueError:
        print('Ввидите целое число')
        exit()

    log_dict = {
            '+' : plus(num_one, num_two),
            '-' : minus(num_one, num_two),
            '*' : multiply(num_one, num_two),
            '/' : divide(num_one, num_two)}

    try:
        print(log_dict[sign])
    except KeyError:
        print('Некорректный знак!')


if __name__ == "__main__":
    main()
