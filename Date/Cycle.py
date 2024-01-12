"""
Class: CS 521 - Spring 1
Date: 2/28/2023
Description of Problem: Creation of an object
that is capable of holding the information needed
to calculate future Werewolf weeks (periods.) 
Uses the Date class. 
"""

from Date import Date

class Cycle():
    """
    Object to track Werewolf Cycles.  
    User inputs dates representing previous werewolf cycles.
    These dates are saved into an input file to be loaded 
    the next time the user interacts with the program. 
    The user can predict when their next werewolf week 
    will be, or they can predict when their current
    werewolf week will end. 
    """
    
    def __init__(self):
        """
        Inputs: None
        Outputs: None
        Function: Initializes the object 
        """
        self.weeks = [] #tracks werewolf weeks
        self.average_length = 5 #average length of werewolf week
        self.average_days_between = 28 # average days in between werewolf weeks
        self.__filename = "werewolf_input.txt"
        
        self.load_file()#automatically load file 
    
    def load_file(self): 
        """
        Inputs: None
        Outputs: None
        Function: loads the input file into the object. 
        """
        
        f = open(self.__filename)
        
        #we could use readlines, but it preserves \n characters
        #which would mess with our object creation
        lines = f.read().splitlines()
        
        if len(lines) == 0:
            self.add_week_string()
            f.close()
            return

        #we do not want any repeated werewolf weeks
        lines = set(lines)
        
        
        for line in lines:
            
            date_strings = line.split("-")
            
        
            start = Date()
            start.load_string(date_strings[0])
            end = Date()
            end.load_string(date_strings[1])
#            
#            print(str(start))
#            print(str(end))
            week = {}
            week["start"] = start
            week["end"] = end
            week["sort"] = start.calculate_num_days()
            self.weeks.append(week)
        
        self.weeks = sorted(self.weeks, key=lambda d: d['sort']) 
        
        if len(self.weeks) > 1:
            self.calculate_average_length()
            self.calculate_average_days_between()
        
        f.close()
    
    def add_week(self, start, end): 
        """
        Inputs: 
            Date - start - start date of Werewolf Week
            Date - end - end date of Werewolf Week
        Outputs:
            String - validation that user added week 
        Function:
            Add user inputted Werewolf Week to the
            instance variables and the input file. 
        """
        
        week = {}
        week["start"] = start
        week["end"] = end 
        week["sort"] = start.calculate_num_days()
        self.weeks.append(week)
        self.weeks = sorted(self.weeks, key=lambda d: d['sort']) 
        
        
        if len(self.weeks) > 1:

            self.calculate_average_length()
            self.calculate_average_days_between()

        week_str = str(start) + " - " + str(end)
        # add the week to the file 
        with open(self.__filename, "a") as f:
#            f.write("\n") #add new line
#            f.write(week_str)
            print(week_str, file=f)
            
        
        return "New week added: " + week_str
        
    
    def calculate_average_length(self):
        """
        Inputs: None
        Outputs: None
        Function: calculate the average lengths of the 
        user's Werewolf Weeks
        """
        
        lengths = [werewolf["end"] - werewolf["start"] for werewolf in self.weeks]
        
        average_length = sum(lengths)/len(lengths)
        self.average_length = int(average_length)
        
    def calculate_average_days_between(self):
        """
        Inputs: None
        Outputs: None
        Function: calculate the average number of days
        between the user's Werewolf Weeks
        """
        
        starts = [werewolf["start"] for werewolf in self.weeks]
        
        
        diffs = []
        for i in range(len(self.weeks)-1):
            start = starts[i]
            next_start = starts[i+1]
            difference = next_start - start 
            print("difference: {}".format(difference))
            diffs.append(difference)
            

        self.average_days_between = int(sum(diffs)/len(diffs))
        
    def get_end_date(self, start_date):
        """
        Inputs: Date - start_date - starting date of Werewolf Week
        Outputs: Date - end date
        Function: Given a start date, predict the end date of
        the user's Werewolf Week 
        """
        
        return start_date.add_days(self.average_length)
        
        
        
    def add_week_string(self):
        """
        Inputs: None
        Outputs: None 
        Function: Prompts the user to enter start 
        and end date strings, converts them into Dates
        and enters them into the Cycle Object
        """
        
        try:
            start_str = input("Please enter the start date of your last werewolf" + " week in (MM/DD/YYYY) format: ")
            start_date = Date()
            start_date.load_string(start_str)

            end_str = input("Please enter the end date of your last werewolf" + " week in (MM/DD/YYYY) format: ")

            end_date = Date()
            end_date.load_string(end_str)
            
        except ValueError:
            print("ValueError: Dates must be positive integers. Dates must be formated in MM/DD/YYYY format. Please try again.")
            
            return self.add_week_string()
        else:
            return self.add_week(start_date, end_date)
        
    def get_next_week(self):
        """
        Inputs: None
        Outputs: Two Tuples representing start and end dates
        Function: Given previous Werewolf Weeks, predict next 
        werewolf week 
        """
        week = self.weeks[-1]  #get last week 
        
        (ns_d, ns_m, ns_y) =  week["start"].add_days(self.average_days_between)
        
        new_start_date = Date(ns_d, ns_m, ns_y)
        
        (ne_d, ne_m, ne_y) = new_start_date.add_days(self.average_length)

        
        return ((ns_d, ns_m, ns_y), (ne_d, ne_m, ne_y))
    
    

    
if __name__ == "__main__":
    
    cycle = Cycle()
    
    start_date = Date( day=29, month=5, year=2023)
    
    ends = cycle.get_end_date(start_date)
    
    end_date = Date(day = ends[0], month = ends[1], year = ends[2])
        
    assert end_date - start_date == cycle.average_length, "Addition of days failed.  End_date is not {} days after start_date".format(cycle.average_length)
    
    print("Get End Date succeeded. ")
    
    
    
    
    