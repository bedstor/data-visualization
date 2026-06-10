import matplotlib.pyplot as plt
print(plt.style.available)


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
# Задание заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Задание размера шрифта и делений на осях
ax.tick_params(labelsize=14)
plt.show()
