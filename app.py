import csv

# def read_file(file_name):
#     read_file = open(file_name, "r")
#     readlines = read_file.readlines()

#     return readlines

def read_file(file_name):
    file = open(file_name, "r")
    rows_of_file = csv.reader(file, delimiter=",")

    return rows_of_file



def search_by_dep(file, dept): # can add a third argument idx(findig by start date index)
    employees = read_file(file)
    matches = []
    for employee in employees:
        if employee[2].upper() == dept.upper():
            matches.append(employee)

    return matches


def search_by_date(file, date):
    employees = read_file(file)
    matches = []
    for employee in employees:
        if employee[3] == date:
            matches.append(employee)

    return matches


def main():
    option = input("1- Search by department\n2- Search by date\n: ")
    if option == "1":
        department = input("Department name: ")
        result = search_by_dep("employees.csv", department)
        for emp in result:
            print(emp)
    if option == "2":
        date = input("Date ex:2020-01-01 : ")
        result = search_by_date("employees.csv", date)
        for emp in result:
            print(emp)


main()