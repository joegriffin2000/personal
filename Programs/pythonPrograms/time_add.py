import datetime as dt
from functools import reduce

sum = []
user = ""

print("Start inserting time values as: minutes,seconds.")
print("Enter \'x\' to sum all current values.")
print("Enter \'q\' to quit.")
while user != "x":
    user = input("\:").strip().lower()
    
    if user == "x":
        break
    elif user == "q":
        break
    elif user.isalnum():
        print("Invalid Entry: Try again.")

    if user.count(",") == 1:
        user = user.split(",")
    elif user.count(",") > 1:
        print("Invalid Entry: Too many values.")
        continue
    else:
        print("Invalid Entry: Too few values.")
        continue

    user = [u.strip() for u in user]

    sum.append(dt.timedelta(
        seconds=int(user[1]),
        minutes=int(user[0])
    ))

if user == "x":
    sum_of_times = reduce(lambda x, y: x + y, sum)
    print(sum_of_times)