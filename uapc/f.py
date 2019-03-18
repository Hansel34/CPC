start_hour, start_minute = [int(x) for x in input().split(':')]
end_hour, end_minute = [int(x) for x in input().split(':')]


print("S",end="")
hours = True
if start_hour == end_hour:
    hours = False
#count downs
elif start_hour > end_hour:
    downs = start_hour - end_hour
    ups = end_hour + 12 - start_hour
else:
    downs = start_hour + 12 - end_hour
    ups = end_hour - start_hour

if hours:
    if ups <= downs:
        print("U"*ups, end = "")
    else:
        print("D"*downs, end = "")

print("S",end="")

minutes = True
if start_minute == end_minute:
    minutes = False
#count downs
elif start_minute > end_minute:
    downs = start_minute - end_minute
    ups = end_minute + 60 - start_minute
else:
    downs = start_minute + 60 - end_minute
    ups = end_minute - start_minute

if minutes:
    if ups <= downs:
        print("U"*ups, end = "")
    else:
        print("D"*downs, end = "")

print("S")

