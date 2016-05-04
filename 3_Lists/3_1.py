__author__ = 'eric'

top_5_names = ["Shane", "Kirby", "Darius", "Ruben", "Godfrey"]

marks = [88, 77, 66, 99]

print "The top 5 names are", top_5_names

top5_songs = ["Just Give Me a Reason", "Can't Hold Us", "When I was your Man", "Gentleman", "Stay"]
print "the top song is", top5_songs[0]


my_list = [101,20,10,50,60]
for item in my_list:
    print item

utensils=["Spoon", "Fork", "Knife"]
for utensil in utensils:
    print utensil

marks = [88, 95, 77, 91]
for mark in marks:
    print mark

my_list = [[2,3], [4,3], [6,7]]
for item in my_list:
    print(item)

top5_songs = ["Just Give Me a Reason", "Can't Hold Us", "When I was your Man", "Gentleman", "Stay"]

for i in range(5):
    print top5_songs[i]


for i in range(len(top5_songs)):
    print top5_songs[i]

for i in range(len(top5_songs)):
    top5_songs[i] = top5_songs[i] +"!"

for i in range(len(top5_songs)):
    print top5_songs[i]

top_5_burger_joints = ["Shake Shack", "Burger Joint", "In-n-Out", "Fresh Burger", "Burger Priest"]

for b in range(len(top_5_burger_joints)):
    print top_5_burger_joints[b]

for b in range(len(top_5_burger_joints)):
    print "{0}. {1}".format(b + 1,top_5_burger_joints[b])