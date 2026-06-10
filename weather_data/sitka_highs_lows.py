from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path("sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение дат, минимальных и максимальных температур из файла
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Создание диаграммы высоких и низких температур
plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="Red", alpha=0.5)
ax.plot(dates, lows, color="Blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="Blue", alpha=0.1)


# Форматирование диаграммы
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatures (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()