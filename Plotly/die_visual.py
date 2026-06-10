import plotly.express as px

from die import Die


# Создание кубика D6
die = Die()

# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результатов
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
title = "Results of Rolling One D6 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.funnel(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()