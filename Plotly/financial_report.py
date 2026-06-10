import plotly.express as px

# Данные: категории и прибыль с них
categories = ["Дизайн карточек", "Принты для худи", "Заказы FastAPI"]
gain = [5000, 3000, 12000]

title = "Financial Report from the Nexus Channel"
fig = px.pie(names=categories, values=gain, title=title)

fig.show()