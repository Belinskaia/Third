#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


# =======================================================================================
# класс 2-мерных векторов
# =======================================================================================
class Vec2d:
    def __init__(self, x1, x2):
        self.x = float(x1)
        self.y = float(x2)

    def __sub__(self, subtr):
        return Vec2d(self.x - subtr.x, self.y - subtr.y)

    def __add__(self, item):
        return Vec2d(self.x + item.x, self.y + item.y)

    def __mul__(self, k):
        return Vec2d(self.x * k, self.y * k)

    def __len__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def int_pair(self):
        return (self.x, self.y)

# =======================================================================================
# класс замкнутых ломаных
# =======================================================================================

class Polyline:
    def __init__(self):
        self.steps = 35
        self.point = []
        self.rate = []

    def add(self, point, speed):
        self.point.append(point)
        self.rate.append(speed)

    def set_points(self):
        """метод перерасчета координат опорных точек"""
        for p in range(len(self.point)):
            self.point[p] = self.point[p] + self.rate[p]
            if self.point[p].x > SCREEN_DIM[0] or self.point[p].x < 0:
                self.rate[p] = Vec2d(- self.rate[p].x, self.rate[p].y)
            if self.point[p].x > SCREEN_DIM[1] or self.point[p].y < 0:
                self.rate[p] = Vec2d(self.rate[p].x, - self.rate[p].y)

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        '''отрисовки точек на экране'''
        for p in self.point:
            pygame.draw.circle(gameDisplay, color, p.int_pair(), width)
        Points = Knot().get_knot(self.points, self.steps)
        '''отрисовка кривой на экране'''
        for p_n in range(-1, len(Points) - 1):
            pygame.draw.line(gameDisplay, color, Points[p_n].int_pair(), Points[p_n + 1].int_pair(), width)

class Knot(Polyline):
    def get_point(self, alpha, deg=None):
        if deg is None:
            deg = len(self.point) - 1
        if deg == 0:
            return self.point[0]
        return self.point[deg]* alpha + Knot().get_point(self.points, alpha, deg - 1) * (1 - alpha)

    def get_points(self, basis, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(Knot().get_point(basis, i * alpha))
        return res

    def get_knot(self, dots, count):
        ''' расчёта точек кривой по добавляемым «опорным» точкам '''
        res = []
        if len(dots) < 3:
            return res
        for i in range(-2, len(dots) - 2):
            ptn = []
            ptn.append((dots[i] + dots[i + 1]) * 0.5)
            ptn.append(dots[i + 1])
            ptn.append((dots[i + 1] + dots[i + 2]) * 0.5)

            res.extend(Knot().get_points(ptn, count))
        return res

# ================================================================
# Функция отрисовки экрана
# =======================================================================================
def draw_help():
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    working = True
    show_help = False
    pause = True
    line = Polyline()

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    line = Polyline()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    line.steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    line.steps -= 1 if line.steps > 1 else 0


            if event.type == pygame.MOUSEBUTTONDOWN:
                line.add(Vec2d(event.pos[0], event.pos[1]), Vec2d(random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        line.draw_points(3, color)
        if not pause:
            line.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
