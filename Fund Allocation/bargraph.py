import plotly.express as px
import pandas as pd
dataframe = pd.read_csv("Integrated_Data.csv")

fig = px.bar(dataframe, x='Name', y='Facility/Demand',
             color = 'Facility/Demand',
             labels={'State':'1'}, height=1000)
fig.show()