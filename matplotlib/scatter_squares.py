import matplotlib.pyplot as plt


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use("bmh")
fig, ax = plt.subplots()
ax.scatter(x=x_values, y=y_values, c=y_values, cmap=plt.cm.rainbow, s=10)

# Задание заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)

# Задание диапазона для каждой оси
ax.axis([0, 1000, 0, 1_100_000])
# Задание формата для меток на осях
ax.ticklabel_format(style="plain")

plt.show()