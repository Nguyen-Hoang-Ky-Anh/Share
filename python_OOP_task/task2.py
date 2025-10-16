class Employee:
    def __init__(self, id, name, birthYear, salaryRate):
        self.__id = id
        self.__name = name
        self.__birthYear = birthYear
        self.__salaryRate = salaryRate

    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getBirthYear(self):
        return self.__birthYear
    
    def getSalaryRate(self):
        return self.__salaryRate
    
    def __str__(self):
        return f"Employee(ID: {self.__id}, Name: {self.__name}, BirthYear: {self.__birthYear}, SalaryRate: {self.__salaryRate})"
    
class Department:
    def __init__(self, name, employees = []):
        self.__name = name
        self.__employees = employees
    
    def getName(self):
        return self.__name
    
    def getEmployees(self) :
        return self.__employees
    
    def setName(self, name):
        self.__name = name
        
    def setEmployees(self, employees):
        self.__employees = employees
    
    # 1) Determine the number of employees having a birth year equal to a given year      
    def countEmployees(self, birthYear):
        return len([emp for emp in self.__employees if emp.getBirthYear() == birthYear])
    
    # 2) Find the oldest employee in the department
    def findOldestEmployee(self):
        return min(self.__employees, key=lambda emp : emp.getBirthYear())
    
    # 3) Make a statistic on the number of employees by birth year, the key is birth year and the value is the number of employees.
    def statByBirthYear(self):
        return {year : len([emp for emp in self.__employees if emp.getBirthYear() == year]) 
                for year in set(emp.getBirthYear() for emp in self.__employees)}

# -----------TEST-----------  
if __name__ == "__main__":
    # Create employee
    e1 = Employee("E01", "Alice", 1990, 2.5)
    e2 = Employee("E02", "Bob", 1985, 3.0)
    e3 = Employee("E03", "Charlie", 1990, 2.0)
    e4 = Employee("E04", "David", 1995, 2.2)

    # Create department
    dept = Department("IT", [e1, e2, e3, e4])
    testYear = 1985
    print(f'Number of employees born in {testYear}: ', dept.countEmployees(testYear))

    oldest = dept.findOldestEmployee()
    print("Oldest employee:", oldest)

    print("Statistic by birth year:", dept.statByBirthYear())
