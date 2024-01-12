"""
Class: CS 521 - Spring 1
Date: 2/26/2023
Description: Creation of a Date class that will hold 
dates in MM/DD/YYYY format.  It can calculate the difference
between two dates. It can validate that Users input dates in the 
correct format 
"""
class Date():
    
    __month_days = [31, 28, 31,30, 31,30, 31, 31, 30, 31, 30, 31]
    
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month 
        self.year = year
        
    
    def load_string(self, date_str):
        """
        Inputs: date_str - string
        Should be in MM/DD/YYYY format. 
        Outputs: None
        Function: Convert MM/DD/YYYY string into
        instance variables day, month, year (ints)
        """
        (month_str, day_str, year_str) = date_str.split("/")

        self.month = int(month_str)

        self.day = int(day_str)

        self.year = int(year_str)   
        
        if (self.month < 1 or self.day < 1 or self.year < 1):
            raise ValueError
        
    def __calculate_num_leap(self):
        """
        Private
        Inputs: int year
        Outputs: number of leap years
        Function: Caclulate the number
        of leap years from 0000 to YYYY where
        YYYY is the year 
        """

        return int(self.year / 4) - int(self.year/100) + int(self.year/400)


    def calculate_num_days(self):
        """
        Inputs: None
        Outputs: number of days from 0/0/0 to self
        Function: Caclulate the number of days from 0/0/0
        to self
        """

        #tracker for how many days 
        # from 0/0/0 to date 
        days = self.day


        #does not include the current month
        #because the day variable stores how many 
        #days have passed that month 
        for m in range(self.month-1):
            days += self.__month_days[m]

        leaps = self.__calculate_num_leap()

        #if its february or january, then the 
        # fact that it's a leap year doesn't matter
        if self.month <= 2:
            leaps -=1

        days += self.year*365 + leaps
        
        return days
    
    def __sub__(self, other):
        """
        Magic Method 
        Inputs: Date - other
        Outputs: int, amount of days in between
        Function: Subtracts two dates to get
        the amount of days between them 
        """
        first = self.calculate_num_days()
        second = other.calculate_num_days()

        
        return first - second
        
    def add_days(self, days):
        """
        Inputs: int - days 
        Outputs: Tuple representing DD/MM/YYY
        Function: Given a date (this object), 
        find the next date after n days inputted
        """
        
        n_day = self.day + days
                
        n_m = self.month 
        
        n_y = self.year
        
        while n_day > self.__month_days[n_m-1]:
            n_day -=  self.__month_days[n_m-1]
            
            n_m += 1
            
            if n_m > 12:
                n_m = 1
                n_y +=1
                
        return(n_day, n_m, n_y)  #usage of tuple
    
    
    def __str__(self):
        """
        Inputs: None
        Outputs: String - MM/DD/YYYY
        Function: Return string representation of date object 
        """
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
                

        
if __name__ == "__main__":
    
    s_date = Date(30,5,2022)
    e_date = Date(4,6,2022)
    
    assert (e_date - s_date) == 5, "Subtraction Unit Test Failed"
    
    print("Subtraction succeeded.  Dates 5 days apart leads to a subtraction that equals 5 days")
    
    new = s_date.add_days(5)
    
    assert (e_date.day == new[0] and e_date.month == new[1]
           and e_date.year == new[2]), "Addition failed. "
    
    print("Addition unit test successed.")