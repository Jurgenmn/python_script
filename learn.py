import csv

def main():
    file = open("employees.csv", "r")
    speamreader = csv.reader(file, delimiter=",")
    for row in speamreader:
        print(row)




main()