'''
Инженерный калькулятор
Напишите программу - инженерный калькулятор. После запуска программа открывает интерактивную оболочку, в которую можно вводить комманды:

user@machine:~$ python calc.py
Advanced calculator. Author: [Student Name], Version: 1.0.0
~ ...
Базовые требования
Программа воспринимает введённые пользователем математические выражения и правильно их интепретирует:
~ 5 + 4
9
~ 10 - 3 + 1
8
~ 2 ** 3 - 1
7
Программа знает о приоритете операторов
~ 2 + 3 * 4
14
~ 8 / 2 * 3
12
Программа поддерживает изменение приоритета при помощи скобок
~ 3 * (2 + 1)
9
~ 5 + (2 - 2 * (3 + 7))
-13
Использование eval, exec, compile запрещено.
Дополнительные баллы (каждый подпункт - 1 балл)
Программа воспринимает основные математические функции и константы:
~ sqrt(3) + ln(e) - pi
-0.4095418460209159
Программа поддерживает переменные
~ x = 5
~ x
5
~ x + 3
8
Программа поддерживает оператор ' для взятия производной простейших функций
~ x = 2
~ (x ** 3)'
12
~ sin(2 * x)'
-0.8322936730942848
Программа поддерживает объявление функций
~ f(x) = x ** 2 + tg(x)'
~ f(5)
37.427881707458354

'''
import re

previous = 0
run = True

class MyClass:

    def advanced_calc(self, expression):

        '''
        Here we write all the logic and return result

        :return:
        '''


        def AdvCalc():

            global run
            global previous

            equation = ""

            if previous == 0:
                equation = input("Введи выражение: ")

            else:
                equation = input(str(previous))

            if equation == 'x':
                print("Пока!")
                exit(0)

            else:
                equation = re.sub('[a-zA-Z,:()" "]', "", equation)

            if previous == 0:
                previous = eval(equation)

            else:
                previous = eval(str(previous) + equation)

        while run:
            AdvCalc()



        return result  # here we return result


if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input('Input Expression: ')

    result = MyClass().advanced_calc(var)

    print(result)
