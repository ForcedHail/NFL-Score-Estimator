from pandas import read_html
import math
import pandas

#user inputs 2 nfl teams abbreviations and year of game simulated
team1name = input("team 1: ")
team2name = input("team 2: ")
year = input("year: ")

# team1name = "was"
# team2name = "crd"
# year = 2023

#grabs tables from link and reads
URL1 = f"https://www.pro-football-reference.com/teams/{team1name}/{year}.htm"
URL2 = f"https://www.pro-football-reference.com/teams/{team2name}/{year}.htm"


team1 = read_html(URL1, attrs={"id": "games"})[0]
team2 = read_html(URL2, attrs={"id": "games"})[0]

#changes nan values (games yet to be played) to 0
def nanTo0(team, col):
    for x in range(len(team.iloc[:,col])):
        if(math.isnan(team.iloc[x,col])):
            team.iloc[x,col] = 0

#counts games played by team
def gamesPlayed(team):
    Ct = 0
    for x in range(len(team.iloc[:,5])):
        if((not(pandas.isnull(team.iloc[x,5])))):
            Ct+=1
    return Ct

team1GP = gamesPlayed(team1)
team2GP = gamesPlayed(team2)

nanTo0(team1,10)
nanTo0(team1,11)
nanTo0(team2,10)
nanTo0(team2,11)

team1AvgPF = sum(team1.iloc[:,10])/team1GP
team1AvgPA = sum(team1.iloc[:,11])/team1GP
team2AvgPF = sum(team2.iloc[:,10])/team2GP
team2AvgPA = sum(team2.iloc[:,11])/team2GP

#formula to predict score of games
team1score = round((team1AvgPF + team2AvgPA)/2)
team2score = round((team2AvgPF + team1AvgPA)/2)
print()
if team1score > team2score:
    print(f"estimate: {team1score} - {team2score} {team1name}")
elif team2score > team1score:
    print(f"estimate: {team2score} - {team1score} {team2name}")
else:
    print("estimate: tie")

#calculate passing yds
nanTo0(team1, 14)
nanTo0(team2, 19)
nanTo0(team1, 19)
nanTo0(team2, 14)
team1PYO = sum(team1.iloc[:,14])/team1GP
team2PYD = sum(team2.iloc[:,19])/team2GP
team2PYO = sum(team2.iloc[:,14])/team2GP
team1PYD = sum(team1.iloc[:,19])/team1GP
print(f"estimated {team1name} pass yds: {(team1PYO+team2PYD)/2}")
print(f"estimated {team2name} pass yds: {(team2PYO+team1PYD)/2}")

#calculate rush yds
nanTo0(team1, 15)
nanTo0(team2, 20)
nanTo0(team1, 20)
nanTo0(team2, 15)
team1RYO = sum(team1.iloc[:,15])/team1GP
team2RYD = sum(team2.iloc[:,20])/team2GP
team2RYO = sum(team2.iloc[:,15])/team2GP
team1RYD = sum(team1.iloc[:,20])/team1GP
print(f"estimated {team1name} rush yds: {(team1RYO+team2RYD)/2}")
print(f"estimated {team2name} rush yds: {(team2RYO+team1RYD)/2}")