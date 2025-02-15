# animals/simulator.py

import random

class InsectSimulator:
    def __init__(self, temperature, food_availability, humidity):
        self.stage = "egg"  # Начинаем как яйцо
        self.temperature = temperature  # Температура (градусы Цельсия)
        self.food_availability = food_availability  # Наличие пищи (0-100, %)
        self.humidity = humidity  # Влажность (0-100, %)
        self.alive = True  # Флаг для отслеживания состояния насекомого
        self.result = []  # Для хранения результата симуляции

    def simulate(self):
        while self.alive:
            if self.stage == "egg":
                self.handle_egg_stage()
            elif self.stage == "larva":
                self.handle_larva_stage()
            elif self.stage == "pupa":
                self.handle_pupa_stage()
            elif self.stage == "adult":
                self.handle_adult_stage()
            else:
                break  # Конец симуляции

    def handle_egg_stage(self):
        if 15 <= self.temperature <= 30:
            self.result.append("Яйцо развивается.")
            self.stage = "larva"
        else:
            self.result.append("Яйцо не развивается из-за неподходящей температуры.")
            self.alive = False

    def handle_larva_stage(self):
        if self.food_availability >= 50:
            self.result.append("Личинка растет.")
            self.stage = "pupa"
        else:
            self.result.append("Личинка погибает из-за недостатка пищи.")
            self.alive = False

    def handle_pupa_stage(self):
        if self.humidity >= 60:
            self.result.append("Куколка формирует взрослое насекомое.")
            self.stage = "adult"
        else:
            self.result.append("Куколка погибает из-за низкой влажности.")
            self.alive = False

    def handle_adult_stage(self):
        lifespan = random.randint(1, 10)  # Случайный срок жизни взрослого насекомого
        self.result.append(f"Взрослое насекомое живет {lifespan} дней.")
        self.alive = False  # Жизненный цикл завершен