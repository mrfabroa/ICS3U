def bigdiff(numlist):

    # set the largest and smallest to default
    largest = numlist[0]
    smallest = numlist[0]

    # iterate throught the list to find the largest and smallest
    for i in range(1,len(numlist)):
        largest = max(largest, numlist[i])
        smallest = min(smallest, numlist[i])

    print(largest)
    print(smallest)

    return largest - smallest


print(bigdiff([3,6,2,4,7]))

