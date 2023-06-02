from math import sqrt


data= {"Jokerit": 9173, "HIFK": 8266, "Kärpät": 5821,
       "TPS": 5534, "Tappara": 5359, "Ilves": 5177}

# getting the mean
total_watchers = 0
#counter
k = 0
for team in data:
    total_watchers = total_watchers + data[team]
    k += 1

print(f"total watchers: {total_watchers}")

mean = total_watchers / k 
print(f"the mean is: {mean}")

# standart deviation 
sd_sum = 0
for team in data:
    dif = mean - data[team]
    sd_sum = sd_sum + (dif**2)

variation = sd_sum / (k - 1)
sd = round(sqrt(variation), 3)
print(f"the standart deviation is: {sd}")

diverging_teams = []

for key,value in data.items():
    if (value - mean)> sd or sd < (mean - value ):
        diverging_teams.append(key)

print("teams that diverge from the mean more than one standard deviation:")
for team in diverging_teams:
    print(team)
