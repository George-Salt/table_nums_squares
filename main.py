import os
import random
from time import sleep, time


def check_answer(user_answer, random_int, time):
    valid_answer = random_int * random_int
    if user_answer == valid_answer:
        print(f"Верно! Тебе понадобилось {time} секунд.")
    else:
        print(f"Неверно! Правильный ответ - {valid_answer}.")


def get_range():
    try:
        int_from = int(input("С какого числа давать задания? "))
        if int_from < 2:
            print("Слишком мало! Буду задвать с 2.")
            int_from = 2
        elif int_from > 80:
            print("Слишком много! Буду задвать с 2.")
            int_from = 2

        int_to = int(input("До какого числа давать задания? "))
        if int_to > 100:
            print("Слишком много! Буду задвать до 100.")
            int_to = 100
        elif int_to < 2:
            print("Слишком много! Буду задвать до 100.")
            int_to = 100

        if int_from > int_to:
            print("Неверный диапазон!")
            int_from = 2
            int_to = 100
        return int_to, int_from
    except ValueError:
        print("Это не число! Буду задавать с 2 до 100")
        sleep(2)
        return 100, 2


if __name__ == "__main__":
    print("Добро пожаловать на практику таблицы квадратов!")
    int_to, int_from = get_range()
    while True:
        try:
            os.system("cls")
            random_int = random.randint(int_from, int_to)
            start_time = time()
            user_answer = int(input(f"Введи квадрат числа {random_int}: "))
            execution_time = int(time() - start_time)
            check_answer(user_answer, random_int, execution_time)
            sleep(2)
        except ValueError:
            print("Это не число!")
            sleep(2)
            continue
