#Chris Taylor
#RTI Exercise
#January 21st, 2021

import csv

#database was changed to a flattened database and then a csv through db browser for sqlLite.
#This was the query used
"""
SELECT
	records.id,
	records.age,
	workclasses.name,
	education_levels.name,
	records.education_num,
	marital_statuses.name,
	occupations.name,
	relationships.name,
	races.name,
	sexes.name,
	records.capital_gain,
	records.capital_loss,
	records.hours_week,
	countries.name,
	records.over_50k
FROM
		records
		INNER JOIN workclasses ON workclasses.id = records.workclass_id
		INNER JOIN education_levels ON education_levels.id = records.education_level_id
		INNER JOIN marital_statuses ON marital_statuses.id = records.marital_status_id
		INNER JOIN occupations ON occupations.id = records.occupation_id
		INNER JOIN relationships ON relationships.id = records.relationship_id
		INNER JOIN races ON races.id = records.race_id
		INNER JOIN sexes ON sexes.id = records.sex_id
		INNER JOIN countries ON countries.id = records.country_id
"""


# draw data from csv
totalHsGrad = 0
hsGrad50k = 0

totalBach = 0
bach50k = 0


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
        
        
print("Only {:d}% of high school graduates make over 50k while {:d}% of college graduates with a bachelors degree make over 50k".format(
    int(hsGrad50k/totalHsGrad * 100), int(bach50k/totalBach * 100)
))

