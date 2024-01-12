"""
Class: CS 521 - Spring 1
Date: 2/28/2023
Description of Problem: Main program from which 
Cycle and Date are called from. 
"""

from Cycle import Cycle
from Date import Date
import sys
    
COMMANDS = [1,2,3,4,5,0, -1]        


def input_functions(input_string, cycle):
    """
    1: Get Next Week 
    2: Enter start date, get likely end date 
    3: Add new werewolf week to system 
    4:  get average length of werwolf week 
    5:  get average number of days in between werewolf weeks 
    0: exit
    
    """
    command = int(input_string) #if this fails, it will raise a value error
    
    if command not in COMMANDS: 
        raise LookupError("Not a valid command.  Commands range" +
                          "from 1-5 for functions," + 
                          "0 for help, and -1 to quit")
    
        return
    
    if command == COMMANDS[0]:
        #get next week
        print("Calculating next predicted Werewolf Week ... ")
        ((ns_d, ns_m, ns_y), (ne_d, ne_m, ne_y)) = cycle.get_next_week()
        
        start_date = str(ns_m) + "/" + str(ns_d) + "/" + str(ns_y)
        
        end_date =  str(ne_m) + "/" + str(ne_d) + "/" + str(ne_y)
        
        return start_date + " - " + end_date
    
    if command == COMMANDS[1]:
        #Next end date
        input_date = input("Please enter the start date of your current" +  " Werewolf Week to predict the end date in MM/DD/YYYY format:")
        
        date = Date()
        date.load_string(input_date)
        (ne_d, ne_m, ne_y) =cycle.get_end_date(date)
        print("Calculating end of your Werewolf Week ... ")
        return(str(ne_m) + "/" + str(ne_d) + "/" + str(ne_y))
    
    if command == COMMANDS[2]:
        # Add week 
        
        
        return cycle.add_week_string()
    
    if command == COMMANDS[3]:
        avg_length = cycle.average_length
        return "Average Length of Werewolf Week is {} days".format(avg_length)
    
    if command == COMMANDS[4]:
        average_days_between = cycle.average_days_between
        return "Average Number of Days Between Werewolf Weeks is {} days".format(average_days_between)
    
    if command == COMMANDS[5]:
        print(str(COMMANDS[0])+": Predict Next Werewolf Week")
        print(str(COMMANDS[1]) + ": Predict End of Werewolf Week")
        print(str(COMMANDS[2]) + ": Add New Werewolf Week to System")
        print(str(COMMANDS[3])+ ": Get Average Length of Werewolf Week")
        print(str(COMMANDS[4])+": Get Average Number of Days Between Werewolf Weeks")
        print(str(COMMANDS[5])+ ": Help")
        print(str(COMMANDS[-1]) + ": Quit Program")
        return "Back to work flow. "
    
    if command == COMMANDS[-1]:
        print("Exiting Program")
        sys.exit()
        
        
        
    
    
if __name__ == "__main__":


    cycle = Cycle()
    
    print("COMMANDS: ")
    print(str(COMMANDS[0])+": Predict Next Werewolf Week")
    print(str(COMMANDS[1]) + ": Predict End of Werewolf Week")
    print(str(COMMANDS[2]) + ": Add New Werewolf Week to System")
    print(str(COMMANDS[3])+ ": Get Average Length of Werewolf Week")
    print(str(COMMANDS[4])+": Get Average Number of Days Between Werewolf Weeks")
    print(str(COMMANDS[5])+ ": Help")
    print(str(COMMANDS[-1]) + ": Quit Program")
    
    while True:
        
        command = input("Please enter a command. ")
        
        print(input_functions(command, cycle))

    