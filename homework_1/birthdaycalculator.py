# Justine Arzola 1804667
# Birthday calculator


print('Birthday Calculator')
print('Current Day')
curr_month = int(input('Month: '))
curr_day = int(input('Day: '))
curr_year = int(input('Year: '))
print('Birthday')
bd_month = int(input('Month: '))
b_day = int(input('Day: '))
bd_year = int(input('Year: '))
years = curr_year - bd_year - 1
if bd_month < curr_month:
    years += 1
elif curr_month == bd_month:
    if b_day < curr_day:
        years += 1
if curr_month == bd_month and curr_day == b_day:
    print('Happy Birthday!')
print('You are '+str(years)+" years old.")
