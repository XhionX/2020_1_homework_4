'''
Флаги
Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n флагов. Изображение одного флага имеет размер 4×4 символов, между двумя соседними флагами также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего флага. Внутри каждого флага должен быть записан его номер — число от 1 до n.

Пример
1.

3

+___ +___ +___
|1 / |2 / |3 /
|__\ |__\ |__\
|    |    |
2.

2

+___ +___
|1 / |2 /
|__\ |__\
|    |

'''


class MyClass:

    def flags(self, expression):

        '''

        Print the flags and return nothing

        :return:
        '''

        while True:
            print('Чтобы остановить введите stop.')
            n = input('Введите количество флагов (от 1 до 9):\n')

            if n == 'stop':
                print('Пока!')
                exit(0)

            n = int(n)

            if n > 9 or n < 1:
                print('Ошибочка, количество флагов должно быть от 1 до 9')

            elif n < 10 and n > 0:

                print('+___ ' * n)

                for i in range(n):
                    print('|', i + 1, ' /', sep='', end=' ')

                print()
                print('|__\\ ' * n)
                print('|    ' * n)


        return



if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input('Input Number of Flags: ')

    result = MyClass().flags(var)
