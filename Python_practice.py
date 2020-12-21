print("Hello World")
counties = ["Arapahoe", "Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if "El Pso" in counties:
    print ("El Paso is in the list of counties.")
else:
    print ("El Paso is not the list of counties.")
if "Arapahoe" in counties or "El Pso" in counties:
    print ("Arapahoe or El Paso is in the list of counties.")
else:
    print ("Arapahoe or El Paso is not in the list of counties.")    
voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters": 422829})
voting_data.append({"county":"Denver","registered_voters": 463353})
voting_data.append({"county":"Jefferson","registered_voters": 432438})
counties = ["Arapahoe", "Denver","Jefferson"]
for county in counties:
    print(county)
numbers = [0,1,2,3,4]
for num in range(5):
    print(num)
counties = ["Arapahoe", "Denver","Jefferson"]
for i in range(len(counties)):
    print(counties[i])
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict.get(county))
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county, voters in counties_dict.items():
    print(county, voters)
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    print(voting_data[i])
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
my_votes = int(input("How many votes did you get in the election?"))

total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes/total_votes*100}% of the total votes.")
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
voting_data = [  {"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")