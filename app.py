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


# def write_employee_to_csv(file_name, name, surname, dpt, sdate):
#     file = open(file_name, "a")  #append
#     csv_row = f"{name},{surname},{dpt},{sdate}\n"
#     file.write(csv_row)

def write_employee_to_csv(file_name, name, surname, dpt, sdate):
    file = open(file_name, "a")
    speamwriter = csv.writer(file, delimiter=",")
    #columns = [name, surname, dpt, sdate]
    speamwriter.writerow([name, surname, dpt, sdate]) #takes a list




def main():
    option = input("1- Search by department\n2- Search by date\n3- Add new employ\n: ")
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

    if option == "3":
        employee_name = input("Name :")
        employee_surname = input("Surname :")
        employee_dpt = input("Department :")
        employee_start_date = input("Start date ex:2020-04-26 :")
        write_employee_to_csv("employees.csv", employee_name, employee_surname, employee_dpt, employee_start_date)



main()