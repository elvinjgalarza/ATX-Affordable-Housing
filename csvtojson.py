import csv

with open('Austin_Affordable_Housing.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    print()
    print("Parsing data...")
    print()
    
    #Put rows into a list
    rows = list(reader)
    
    #row iterator
    i = 0
    for c in rows:
        if row[i]