import plotly.express as px

# Данные в виде списков
weight_x = [60, 70, 80, 90, 100]
age_y = [18, 25, 30, 42, 50]
kallories_z = [300, 400, 450, 550, 700]

# Строим 3D-график
fig = px.scatter_3d(x=weight_x, y=age_y, z=kallories_z)
fig.show()