import matplotlib.pyplot as plt

# Данные для визуализации
x = [1, 2, 3]
y = [1, 5, 9]

plt.style.use("bmh")
fid, ax = plt.subplots()
ax.plot(x, y, c="Red", linewidth=2, marker="o")

ax.set_xlabel("День июня", fontsize=14)
ax.set_ylabel("Уровень боли", fontsize=14)

plt.show()