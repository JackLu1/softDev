import csv
import random

# Builds dictionary of occupations and corresponding percentage of workforce.
def buildDict(filename):
    d = {}
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile)
        first = reader.__next__() # Processes column labels Job Class, Percentage
        d[first[0]] = first[1]
        for i in reader:
            d[ i[0] ] = float( i[1])
    return d

# Choose random job based on percentage
def chooseRandom(dictionary):
    jobList = list(dictionary.keys()) # list of jobs
    chanceList = list(dictionary.values()) # list of percentages
    # Ignores first and last rows (heading and total)
    randJob = random.choices(jobList[1:-1], chanceList[1:-1])[0]
    return randJob