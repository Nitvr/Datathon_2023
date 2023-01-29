import pandas as pd

dataframe = pd.read_csv("sc-est2019-agesex-civ.csv")

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

dict = {}
for x in dataframe.index:
    num = dataframe.loc[x,"POPEST2019_CIV"]
    sex = dataframe.loc[x,"SEX"]
    age = dataframe.loc[x,"AGE"]
    state = dataframe.loc[x,"NAME"]
    if age != 999 or sex != 0:
        continue
    dict[state] = num

name = []
population = []
sum = 0
for x in dict.keys():
    if x=="United States":
        name.append("Total")
        population.append(dict[x])
        continue
    name.append(x)
    population.append(dict[x])

pop_distribution = {"Name":name, "Demand":population }
df = pd.DataFrame(pop_distribution)
df.to_csv("Population_2019.csv")