
# 1. Import the necessary modules
import csv
import copy
import random

# 2. Defining the dictionary template
data_template = {'date': '', 'new': 0, 'deaths': 0, 'recovered': 0}

# 3. Opening the CSV file and reading the data
data_list = []
with open('C:/Users/dci-student/Desktop/PYTHON/day5-Wed.12/covid_data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
#    print(csv_reader.fieldnames)
    for row in csv_reader:
        data = copy.deepcopy(data_template)
        data['date'] = row['date']
        data['new'] = int(row['new'])
        data['deaths'] = int(row['deaths'])
        data['recovered'] = int(row['recovered'])
        data_list.append(data)

# 4. Calculating and printing the total number of cases, deaths, and recoveries
total_cases = 0
total_deaths = 0
total_recoveries = 0

for data in data_list:
    total_cases += data['new']
    total_deaths += data['deaths']
    total_recoveries += data['recovered']

print(f"Total cases: {total_cases}")
print(f"Total deaths: {total_deaths}")
print(f"Total recoveries: {total_recoveries}")

# 5. Calculating the average number of new cases per day
num_days = 0
for data in data_list:
    num_days += 1

total_new_cases = total_cases
average_new_cases = total_new_cases / num_days

print(f"Average new cases per day: {average_new_cases}")

# 6. Selecting a Random Day from the Data and Printing the Data for That Day
random_day = random.choice(data_list)
print(f"Random Day: {random_day['date']}")
print(f"New Cases: {random_day['new']}")
print(f"Deaths: {random_day['deaths']}")
print(f"Recoveries: {random_day['recovered']}")
