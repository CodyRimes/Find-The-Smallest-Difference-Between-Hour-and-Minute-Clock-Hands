#This program will take in the users input for the hour hand and minute hand (by the time on the clock)
#And will calculate shortest difference in distance by degrees between the two hands (there would be two ways to measure the distance in degrees on a clock, you could go around the long way, or go the shorter way between the two hands)


hourHandInputResponse = input("Please enter the time on your clock. First we will take the input of the hour hand: ")
#Python F statements (note the F before the quotation marks begin) allow us to print variables within a print function/statement, thus allowing the print statement to be dynamic, and not hard coded/static
print(f"The number we received was, {hourHandInputResponse}")

minuteHandInputResponse = input("Please enter the input for the minute hand on your clock: ")
print(f"The number we received was, {minuteHandInputResponse}")

#This function calculates the smallest difference in degrees between the hour hand and the minute hand
#Receives the time input for the hour hand and the minute hand
#Returns calculated smallest degree difference between the two hands
def calculateSmallestDifferenceInDegreesBetweenMinuteAndHourHandOnTheClock(hourHandInputResponse:int, minuteHandInputResponse:int) -> int:
    #We will have to do some logical arithmetic to get to where we need to go with this problem
    #We know that one revolution is 360 degrees
    #We know that there are 60 minutes for 1 revolution on the clock by the minute hand
    #We know that there are 12 hours for 1 revolution on the clock by the hour hand

    #Lets figure out how many degrees the minute hand moves for one minute (thus we will know how many degrees there are per minute)
    #360 degrees / 60 minutes = 6 degrees is moved with each passing minute, i.e. 6 degrees per minute
    #While the minute hand moves faster than the hour hand, we know that the hour hand should be moving even slower (even less degrees moved per minute), thus we need to divide the 60 minutes minutes by each hour
    #360 degree / 60 minutes / 12 hours, or said another way, 360 degrees / 60 minutes = 6 degrees per minute; 6 degrees per minute / 12 hours = 0.5 degrees moved per minute for the hour hand
