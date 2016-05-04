__author__ = 'eric'

players = []

players.append(["Player", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"])
players.append(["Lebron James", 19.1, 23.1, 26.5, 24.1, 26.8])
players.append(["Michael Jordan", 26.5, 32.6, 33.4, 31.2, 29.1])
players.append(["Kobe Bryant", 17.6, 21.4, 18.9, 21.2, 25.1])
players.append(["Kevin Durant", 21.1, 23.3, 27.5, 25.6, 26.2])

print players[0][3]

for r in range(len(players)):
    for c in range(len(players[r])):
        print players[r][c]

# Your Try 1: Print out the values of the first row of the players table.
for i in range(len(players)+1):
    print players[0][i]

#alternatively
for row in players[0]:
    print row

# You Try 2: Print out the values of the first column of the players table.
for row in players:
    print row[0]

print ""
#
# You Try 3: print out the values of the last two rows, one item per line.
for r in range(len(players)-2, len(players)):
    for c in range(len(players[r])):
        print players[r][c]


# example 2
print "EXAMPLE 2"
total = 0
count = 0

for data_row in range(1, len(players)):
    for data_column in range(1, len(players[data_row])):
        total += players[data_row][data_column]
        count += 1

    player_avg = total/float(count)
print player_avg
