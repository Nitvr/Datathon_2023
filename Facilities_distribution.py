import pandas as pd



csv_head = ["Unnamed: 9","Fax","Phone","Zip Code","State"]
facilities_in_states = {}
facilities_out_states = {}
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

dataframe = pd.read_csv("beginner.csv")
#print(dataframe)
in_state_count = 0
out_state_count = 0
for x in dataframe.index:
    for head in csv_head:
        str = dataframe.loc[x,head]
        if type(str) == type("1") and len(str) == 2:
            if str in states.keys():
                str = states[str]
                in_state_count += 1
                if str not in facilities_in_states:
                    facilities_in_states[str] = 1
                else:
                    facilities_in_states[str] += 1
            else:
                out_state_count += 1
                if str not in facilities_out_states:
                    facilities_out_states[str] = 1
                else:
                    facilities_out_states[str] += 1
            break

#in-states distribution to cvs
Name = []
Facility_count = []
for state in facilities_in_states.keys():
    Name.append(state)
    Facility_count.append(facilities_in_states[state])

Name.append("Total")
Facility_count.append(in_state_count)

distribution_data = {'Name': Name, 'Facility Count': Facility_count}
distribution = pd.DataFrame(distribution_data)

distribution.to_csv('Facility_distribution.csv')

#out-states distribution to cvs
Name = []
Facility_count = []
for state in facilities_out_states.keys():
    Name.append(state)
    Facility_count.append(facilities_out_states[state])

Name.append("Total")
Facility_count.append(out_state_count)

distribution_data = {'Name': Name, 'Facility Count': Facility_count}
distribution = pd.DataFrame(distribution_data)

distribution.to_csv('Extra_facility.csv')