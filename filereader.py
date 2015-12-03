import csv
with open('All partners.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row