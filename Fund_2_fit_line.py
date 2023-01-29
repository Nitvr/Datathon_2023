import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np

dataframe = pd.read_csv("Integrated_Data.csv")


fig = go.Figure(data=go.Scatter(
    x=dataframe["Demand"], y=dataframe["Facility Count"],
    mode='markers',
    marker=dict(
        size=12,
        color=np.random.randn(500), #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    )
))

fig.show()



def test(x,y,a):
    sum = 0
    for i in range(len(x)):
        sum += (y[i] - (a*x[i]))**2
    return sum

demand = []
facility = []

for x in dataframe.index:
    demand.append(float(dataframe.loc[x, "Demand"]))
    facility.append(float(dataframe.loc[x, "Facility Count"]))

minn = float('inf')
mina = 0.0
for a in range(1000000,10000000):
    a0 = float(a/100000000000.0)
    sq = test(demand, facility, a0)
    if sq < minn:
        minn = sq
        mina = a0


print(mina)

def predict(x):
    return x*mina
name = []
shortage = []
sum = 0
for x in dataframe.index:
    x_demand = float(dataframe.loc[x, "Demand"])
    x_facility = float(dataframe.loc[x, "Facility Count"])
    if x_facility < predict(x_demand):
        name.append(dataframe.loc[x, "Name"])
        shortage.append((predict(x_demand) - x_facility))


fig = px.pie(values=shortage, names=name, color_discrete_sequence=px.colors.sequential.RdBu)
fig.show()
