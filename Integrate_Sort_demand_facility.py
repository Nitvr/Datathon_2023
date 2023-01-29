import pandas as pd

facility = pd.read_csv("Facility_distribution.csv")
demand = pd.read_csv("Demand_2020.csv")

facility_per_demand = {}

dict = {}

for x in facility.index:
    state_name = facility.loc[x, 'Name']
    state_facility = facility.loc[x, 'Facility Count']
    if state_name not in dict.keys():
        dict[state_name] = [state_facility]

for x in demand.index:
    state_name = demand.loc[x, 'Name']
    state_demand = demand.loc[x, 'Demand']
    dict[state_name].append(state_demand)


for state in dict.keys():
    dict[state].append(float(dict[state][0])/float(dict[state][1]))

sort_dict = sorted(dict.items(), key=lambda item: item[1][2])


state_file = []
facility_file = []
demand_file = []
fpd_file = []
for item in sort_dict:
    if item[0] == "Total":
        continue
    state_file.append(item[0])
    facility_file.append(item[1][0])
    demand_file.append(item[1][1])
    fpd_file.append(item[1][2])

dict_file = {"Name":state_file,"Facility Count":facility_file,"Demand":demand_file,"Facility/Demand":fpd_file}
df = pd.DataFrame(dict_file)
df.to_csv("Integrated_Data.csv")



