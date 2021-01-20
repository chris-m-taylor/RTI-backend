#Chris Taylor
#RTI Exercise
#January 21st, 2021

import csv

# draw data from csv

#Benefits of School
totalHsGrad = 0
hsGrad50k = 0

totalBach = 0
bach50k = 0

#Gender Equality
totalMen = 0
totalWomen = 0

men50k = 0
women50k = 0

#Government vs Private pay vs Self Employed
totalGov = 0
totalPrivate = 0
totalSelfEm = 0

gov50k = 0
private50k = 0
selfEm50k = 0


with open('flat-csvV2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['education_level'])

        if (row['education_level'] == 'HS-grad'):
            totalHsGrad += 1
            if (row['over_50k'] == '1'):
                hsGrad50k += 1

        # add total number of bachelors degrees and get the amount that is over 50k
        elif (row['education_level'] == 'Bachelors'):
            totalBach += 1
            if (row['over_50k'] == '1'):
                bach50k += 1

        # Gender stats
        if (row['sex'] == 'Male'):
            totalMen += 1
            if (row['over_50k'] == '1'):
                men50k += 1
        
        elif (row['sex'] == 'Female'):
            totalWomen += 1
            if (row['over_50k'] == '1'):
                women50k += 1

        # government vs private pay vs self employed
        if (row['workclass'][-3:] == 'gov'):
            totalGov += 1
            if (row['over_50k'] == '1'):
                gov50k += 1
        
        elif (row['workclass'] == 'Private'):
            totalPrivate += 1
            if (row['over_50k'] == '1'):
                private50k += 1
        else:
            totalSelfEm += 1
            if (row['over_50k'] == '1'):
                selfEm50k += 1

        
print("Only {:d}% of high school graduates make over 50k while {:d}% of college graduates with a bachelors degree make over 50k".format(
    int(hsGrad50k/totalHsGrad * 100), int(bach50k/totalBach * 100)
))

print("Only {:d}% of women make over 50k while {:d}% of men make over 50k".format(
    int(women50k/totalWomen * 100), int(men50k/totalMen * 100)
))

print("{:d}% of government workers make over 50k, {:d}% of private sector employees make over 50k, and {:d}% of self employed individuals make over 50k".format(
    int(gov50k/totalGov * 100), int(private50k/totalPrivate * 100), int(selfEm50k/totalSelfEm * 100)
))
