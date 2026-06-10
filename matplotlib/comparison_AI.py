import matplotlib.pyplot as plt

# Данные: эпохи обучения и точность моделей
learning = []
for era in range(1, 6):
    learning.append(era)

accuracy_line_1 = [50, 70, 85, 90, 95]
accuracy_line_2 = [40, 55, 65, 75, 80]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(learning, accuracy_line_1, c="Green", linestyle="--", label="Model A", linewidth=4)
ax.plot(learning, accuracy_line_2, c="Blue", label="Model B", linewidth=4)
# Создание легенды 
ax.legend()

# Задание заголовков
title = "Comparing A and B Machine Learning Model"
ax.set_title(title, fontsize=18, color="Red")
ax.set_xlabel("Eras of Learning", fontsize=12)
ax.set_ylabel("Accuracy", fontsize=12)

plt.show()