import random
import math
#возьмем встроенную библиотеку random для случайных значений
inches = 40
centemitre = 101.6

def kid_neuro(epoch, lr, accur):
    """
    :param epoch:  - сколькко раз у нас она попробует вычислить правильное значени
    :param lr:  - с каким шагом наша нейросеть у нас будет обучаться
    :param accur:  - насколько точный нас устроит результат
    :return:
    """
    W_coef = random.uniform(1, 3) # мы значем, что правильный ответ это около 2.54 возьмем числа около того наугад
    print(f"Наш первоначальный вес равен {W_coef}") #чтобы понимать, что нам выкинул рандом

    for i in range(epoch):
        Error = centemitre - (inches * W_coef) # error насколько у нас наша нейросеть ошиблась
        print(f"Наша ошибка составляет {Error}")

        if abs(Error) < accur:
            print(f"Наш итоговый результат {W_coef}")
        if Error > 0:
            W_coef += lr
            #если ошибка положительная нам нужн наращивать вес
        elif Error < 0:
            W_coef -= lr
