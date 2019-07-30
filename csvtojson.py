import csv

file = open("wampus.txt", "w+")
file.write("[")

with open('Austin_Affordable_Housing.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    print()
    print("Parsing data...")
    print()
    
    #Put excel into a list
    excel = list(reader)

    #excel[X][2] is for project name
    #excel[X][6] is for zip codes
    #excel[X][12] is for tenure types (i.e., rental)
    #excel[X][56] is for location(lat,lon)
    #excel iterator
    i = 0
    n = 1
    for row in excel:
        if excel[i][6] == "78,705":
            if excel[i][12] == "Rental":
                #ID
                file.write('{"ID":')
                file.write('%d' %n)
                n+=1
                file.write(',')

                #Name
                file.write('"Name:""')
                file.write(excel[i][2])
                file.write('",')

                #Address
                file.write('"Address:""')
                file.write(excel[i][5])
                file.write('",')

                #Zip Code
                file.write('"Zip Code":"78705",')

                #Total Units 
                file.write('"Total Units:""')
                file.write(excel[i][8])
                file.write('",')

                #Total Affordable Units
                file.write('"Total Affordable Units:""')
                file.write(excel[i][9])
                file.write('",')

                #Owner
                file.write('"Owner:""')
                file.write(excel[i][3])
                file.write('",')

                #Developer
                file.write('"Developer""')
                file.write(excel[i][4])
                file.write('",')

                #Latitude
                file.write('"lat:"')
                file.write(excel[i][55])
                file.write(',')

                #Longitude
                file.write('"lng:"')
                file.write(excel[i][54])
                #file.write('"')
                file.write("}")
                if n > 1 and n < 66:
                    file.write(",")

                #file.write(excel[i][56]) 
        i+=1

    file.write("]")
    file.close()