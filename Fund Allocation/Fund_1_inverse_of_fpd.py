import pandas as pd
import plotly.express as px

dataframe = pd.read_csv("Integrated_Data.csv")

name = []
inverse = []
sum = 0
for x in dataframe.index:
    name.append(dataframe.loc[x, "Name"])
    inverse.append(1.0/float(dataframe.loc[x, "Facility/Demand"]))
    sum += float(dataframe.loc[x, "Facility/Demand"])

for i in range(len(inverse)):
    inverse[i] = inverse[i]/sum



fig = px.pie(values=inverse, names=name, color_discrete_sequence=px.colors.sequential.RdBu)
fig.show()

