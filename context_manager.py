
import datetime


class FileOpener:

    def __init__(self, file_path):

        global begining_time
        begining_time = datetime.datetime.now()
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        ending_time = datetime.datetime.now()
        print(f"время запуска кода: {begining_time}")
        print(f"время окончания работы кода: {ending_time}")
        print(f"время работы кода: {ending_time - begining_time}")
        self.file.close()


with FileOpener("recipes.txt") as file:
    data = file.read()
    print(f"Распечатываем книгу рецептов: ")
    print(data)
    print()


# Необходимо реализовать менеджер контекста, печатающий на экран:
#
# Время запуска кода в менеджере контекста;
# Время окончания работы кода;
# Сколько было потрачено времени на выполнение кода.
#
# Придумать и написать программу, использующая менеджер контекста из задания
# Если придумать не получиться, использовать программу из предыдущих домашних работ.
#
# Для подготовки к следующей лекции прочитайте про форматы данных json, xml, csv.
