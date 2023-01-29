import pandas as pd

population = pd.read_csv("2020_population_prediction.csv")
weight = pd.read_csv("weight_evaluation.csv")

weight_dict = {}
for x in weight.index:
    age = weight.loc[x,"Age"]
    gender = 0
    if weight.loc[x,"Sex Code"] == "F":
        gender = 2
    else:
        gender = 1
    weight_dict[(gender,age)] = weight.loc[x,"S Rate"]

for i in range(13):
    age = i*5+20
    for j in range(5):
        weight_dict[(2,age+j)] = weight_dict[(2,age)]

for i in range(7):
    age = i * 5 + 50
    for j in range(5):
        weight_dict[(1, age + j)] = weight_dict[(1, age)]

print(weight_dict)

state_demand = {}
for x in population.index:
    state = population.loc[x, "NAME"]
    if state not in state_demand.keys():
        state_demand[state] = 0
    age = population.loc[x, "AGE"]
    gender = population.loc[x, "SEX"]
    number = population.loc[x, "2020_Population"]
    if gender == 1:
        if age < 50 or age > 85:
            continue
        state_demand[state] += number * weight_dict[(1,age)]
    if gender == 2:
        if age < 20 or age > 85:
            continue
        state_demand[state] += number * weight_dict[(2, age)]

print(state_demand)

name = []
demand_2020 = []
for state in state_demand.keys():
    if state == "United States":
        name.append("Total")
    else:
        name.append(state)
    demand_2020.append(state_demand[state])

demand_dict = {"Name":name,"Demand":demand_2020}
df = pd.DataFrame(demand_dict)
df.to_csv("Demand_2020.csv")

