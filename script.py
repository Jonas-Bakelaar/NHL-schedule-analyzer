import csv
import datetime

def getScheduleForTeam(teamName):
    with open("2023_2024_NHL_Schedule.csv", newline='') as csvfile:
        schedule = csv.reader(csvfile, delimiter=",", quotechar='|')

        games = []

        for row in schedule:
            # print(', '.join(row))
            if teamName in row:
                games.append(row)
        
        return games

def getNumberOfBackToBacks(schedules, team):
    dates = []
    for games in schedules[team]:
        try:
            dates.append(datetime.datetime.strptime(games[0], "%Y-%m-%d"))
        except:
            dates.append(datetime.datetime.strptime(games[0], "%m-%d-%Y"))

        # elif datetime.datetime.strptime(games[0], "%m-%d-%Y"):
        #     dates.append(datetime.datetime.strptime(games[0], "%m-%d-%Y"))
    
    count = 0
    bothAtHome = 0
    bothAway = 0

    for index, date in enumerate(dates):
        dateComparison = date + datetime.timedelta(days=1)
        if (index+1) < 82:
            if dates[index+1] == dateComparison:
                count = count+1
                # print("b2b for", team)
                # print(schedules[team][index])
                # print(schedules[team][index+1])

                if(schedules[team][index][3] == team and schedules[team][index+1][2] == team):
                    bothAtHome = bothAtHome + 1
                
                if(schedules[team][index][2] == team and schedules[team][index+1][2] == team):
                    bothAway = bothAway + 1
                    
    print(team, "has", count, "back to backs", bothAtHome, "of which are both at home, and", bothAway, "are both away")


def main():
    with open("nhlTeams.txt", newline='') as teamsFile:
        teams = teamsFile.readlines()
    
    schedules = {}
    for team in teams:
        team = team.strip("\r\n")
        schedules[team] = getScheduleForTeam(team)
        getNumberOfBackToBacks(schedules, team)

if __name__ == "__main__":
    main()
