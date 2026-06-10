import plotly.express as px


weight = [60, 70, 80, 90, 100]
calories = [300, 420, 510, 630, 720]

fig = px.scatter(x=weight, y=calories)
fig.show()