import plotly.express as px

x_value = [1, 2, 3]
y_value = [2, 5, 0]
title = "Number of Uploaded Works"
labels = {"x": "Days", "y": "Works"}
fig = px.bar(x=x_value, y=y_value, title=title, labels=labels)
fig.show()