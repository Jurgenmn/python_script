import csv

def main():
    file = open("employees.csv", "r")
    rows = list(csv.reader(file, delimiter=","))
    count = 0
    # speamreader[0].insert(0, "id")
    # print(speamreader[0])
    for i in range(len(rows)):
        if i == 0:
            rows[i].insert(0, "id")
        else:
            rows[i].insert(0, count)

        count += 1
        #print(rows[i])

    file = open("employees.csv", "w")
    writer = csv.writer(file, delimiter=",")
    for row in rows:    #rows is list of lists
        writer.writerow(row)

    
main()