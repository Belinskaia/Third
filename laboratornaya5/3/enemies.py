# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    def annoying_input_int(message=''):
        answer = None
        while answer == None:
            try:
                answer = list(map(int, input(message).split(',')))
            except ValueError:
                print('Вы ввели недопустимые символы')
        if len(answer) == 1:
            return answer[0]
        return answer


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class BlueTroll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'синий'

    def question(self):
        x = randint(1, 5)
        self.__quest = "Угадай число от 1 до 5"
        self.set_answer(x)
        return self.__quest


class PinkTroll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'малиновый'
    def question(self):
        def prime_number(f):
            for i in range(2, f // 2 + 1):
                if (f % i == 0):
                    return 0
            return 1
        x = randint(1, 100)
        self.__quest = str(x) + " - простое число? (формат ответа: 1/0)"
        self.set_answer(prime_number(x))
        return self.__quest


class GrayTroll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'серый'

    def question(self):
        def multiplier (m):
            answer = []
            g = 2
            while g * g <= m:
                if m % g == 0:
                    answer.append(g)
                    m //= g
                else:
                    g += 1
            if m > 1:
                answer.append(m)
            return answer
        x = randint(1, 100)
        self.__quest = "Разложи число " + str(x) + " на множители и перечисли их через запятую в порядке возрастания (без 1)."
        ans = multiplier(x)
        self.set_answer(ans)
        return self.__quest

enemy_types = [GreenDragon, RedDragon, BlackDragon, PinkTroll, BlueTroll, GrayTroll]