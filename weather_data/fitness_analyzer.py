from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


def on_close(event):
    """Сделанные шаги за неделю, максимальное количество за день и совет"""
    print(f"Общее количество шагов за неделю: {sum(steps)}")
    print(f"Максимальное количество шагов за день: {max(steps)}")
    if sum(steps) < 60_000:
        print("Совет: Нужно двигаться больше! Постарайся ходить чаще")
    else:
        print("Совет: Отличная работа! Ты держишь высокую активность")


path = Path("fitness_data.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение дат, количества шагов и калорий из файла
dates, steps, calories = [], [], []
for row in reader:
    date = datetime.strptime(row[0], '%Y-%m-%d')
    step = int(row[1])
    calories_burned = step * 0.04
    dates.append(date)
    steps.append(step)
    calories.append(calories_burned)

# Строим шаги на левой оси Y
fig, ax1 = plt.subplots()
ax1.plot(dates, steps, label="Шаги", linewidth=2, color="Orange")
ax1.set_ylabel("Количество шагов", color="Orange", fontsize=14)
ax1.tick_params(axis='y', labelcolor="Orange")

# Создаём вторую (правую) ось Y
ax2 = ax1.twinx()

# Строим калории на правой оси Y
ax2.plot(
    dates, calories, label="Калории", linewidth=2, color="Red", linestyle='--'
)
ax2.set_ylabel("Соженные калории", color="Red", fontsize=14)
ax2.tick_params(axis='y', labelcolor="Red")

# Форматирование
title = "Динамика шагов и калорий за неделю"
ax1.set_title(title, fontsize=18)
ax1.set_xlabel("Дата", fontsize=14)
fig.autofmt_xdate()

# Привязываем событие закрытия к функции
fig.canvas.mpl_connect("close_event", on_close)

plt.show()
