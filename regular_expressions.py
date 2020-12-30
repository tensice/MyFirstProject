import re
search_string = '780m'
my_string = r'(\d*)([dmwy])'
pattern = re.compile(my_string)
match = pattern.match(search_string)
if match:
    num = match.group(1)
    time = match.group(2)
    if time == 'd':
        expanded_time = 'day'
    elif time == 'w':
        expanded_time = 'week'
    elif time == 'm':
        expanded_time = 'month'
    elif time == 'y':
        expanded_time = 'year'
    print(f'{num} {expanded_time}')
else:
    print('Irregular input')











# my_string = r'\d+:\d\d'
# print(my_string)
# pattern = re.compile(my_string)
# search_text = '''
# Liverpool lost 2-0 to Atalanta in the Champions League on Wednesday after resting several first-team regulars.
# Three teams have played on Saturday at 12:30 after a Wednesday Champions League match - Manchester City, Manchester United and Liverpool, once each.
# Tottenham have played a Sunday 12:00 game after a Thursday night Europa League match, which is a similar turnaround.
# Liverpool's other 12:30 Saturday game this season - a 2-2 draw with Everton - came directly after an international break.
# They have another one next month when they play title rivals Tottenham on Wednesday, 16 December before facing Crystal Palace in the early Saturday slot.
# "Why did you
# '''
# clock = '12:59'
# #matches = pattern.finditer(search_text)
# match = pattern.match(clock)
# if match:
#     print(match.group())
# else:
#     print('no match')
# # for match in matches:
# #     print(match)
# #print(search_text[575:581])


