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
        
        if (row['sex'] == 'Female'):
            totalWomen += 1
            if (row['over_50k'] == '1'):
                women50k += 1
        
        
print("Only {:d}% of high school graduates make over 50k while {:d}% of college graduates with a bachelors degree make over 50k".format(
    int(hsGrad50k/totalHsGrad * 100), int(bach50k/totalBach * 100)
))

print("Only {:d}% of women make over 50k while {:d}% of men make over 50k".format(
    int(women50k/totalWomen * 100), int(men50k/totalMen * 100)
))

