import csv
with open('Book1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Bob'])
    