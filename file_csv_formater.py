# csv = comma separated values
import csv
from datetime import datetime
path = 'data/superbowl.csv'
with open(path,newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data =[row for row in reader]
print(header)
print(data[0])

sb_list = []
for d in data:
    sb_dict = {}
    d1 = datetime.strptime(d[0],'%b %d %Y')
    sb = d[1].split()
    sb_roman = sb[0]
    sb_int = int(sb[1][1:-1])
    winner = d[2]
    winner_pts = int(d[3])
    loser = d[4]
    loser_pts = int(d[5])
    mvp = d[6]
    stadium = d[7]
    city = d[8]
    state = d[9]
    sb_dict[header[0]] = d1
    sb_dict['sb_roman'] = sb_roman
    sb_dict['sb_int'] = sb_int
    sb_dict[header[2]] = winner
    sb_dict[header[3]] = winner_pts
    sb_dict[header[4]] = loser
    sb_dict[header[5]] = loser_pts
    sb_dict[header[6]] = mvp
    sb_dict[header[7]] = stadium
    sb_dict[header[8]] = city
    sb_dict[header[9]] = state
    sb_list.append(sb_dict)

print(sb_list)
