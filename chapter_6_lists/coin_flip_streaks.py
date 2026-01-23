import random
number_of_streaks = 0
for experiment_number in range(1000):
    flips = []
    for i in range(100):
        flips.append(random.choice(['T','H']))

    streak_found = False
    for i in range(len(flips)-5):
        if flips[i:i+6]==['T']*6 or flips[i:i+6]==['H']*6:
            streak_found = True
            break
    if streak_found:
        number_of_streaks += 1

print('Chance of streak: %s%%' % (number_of_streaks /  100))