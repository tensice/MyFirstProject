import csv
from datetime import datetime
#csv means comma, separated, value
path = 'data/superbowl.csv'
with open(path) as file:
    reader = csv.reader(file)
    header = next(reader)
    data = [i for i in reader]
print(header)
sb_list = []
for d in data:
    sb_dict = {}
    sb_date = datetime.strptime(d[0],'%b %d %Y')
    sb_split = d[1].split(" ")
    sb_roman = sb_split[0]
    sb_int = int(sb_split[1][1:-1])
    winner = d[2]
    winner_pts = int(d[3])
    loser = d[4]
    loser_pts = int(d[5])
    mvp = d[6]
    stadium = d[7]
    city = d[8]
    state = d[9]
    print(sb_date)
    print(sb_roman)
    print(sb_int)
    sb_dict[header[0]] = sb_date
    sb_dict['sb_roman'] = sb_roman
    sb_dict['sb_int'] = sb_int
    sb_dict['winner'] = winner
    sb_dict['winner_pts'] = winner_pts
    sb_dict['loser'] = loser
    sb_dict['loser_pts'] = loser_pts
    sb_dict['mvp'] = mvp
    sb_dict['stadium'] = stadium
    sb_dict['city'] = city
    sb_dict['state'] = state
    print(sb_dict)
    sb_list.append(sb_dict)



#Which state held the most superbowls?
#Which player got the most mvp's
#Which winning team had the most points








