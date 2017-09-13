#!/usr/bin/env python
"""This program calculates the number of years you need to work before you can retire based on your salary"""

NUMBER_OF_WEEKS_IN_A_WORK_YEAR = 52
NUMBER_OF_WORK_HOURS_IN_A_WEEK = 40
HOURS_WORKED_IN_A_YEAR = 1920

def CalculateAnnualWage(hourly_rate, hours_worked=(NUMBER_OF_WEEKS_IN_A_WORK_YEAR * NUMBER_OF_WORK_HOURS_IN_A_WEEK)):
    return hourly_rate * hours_worked

def CalculateRetirement(money_needed_to_retire=100000,yearly_salary=20000):
    if money_needed_to_retire % yearly_salary == 0:
        print('\033[94m' + 'number of years to retire is even' + '\033[94m')
    elif money_needed_to_retire % yearly_salary != 0:
        #print 'number of years to retire is odd'
        print('\033[94m' + 'number of years to retire is odd' + '\033[94m')
    return money_needed_to_retire / yearly_salary

def GetJobInfo():

    while True: # True/False are keywords.
        said = raw_input('what is your dream job? : ')
        try:
            said = str(said)
        except ValueError:
            print said, "this is not a job description try again"
            continue
        hourly_wage = raw_input('what is your hourly wage? :')
        try:
            hourly_wage = float(hourly_wage)
        except ValueError:
            print hourly_wage, 'is not a wage ! Please try again.'
            continue
        money_needed_to_retire = raw_input('How much money do you need to retire in style? : ')
        try:
            money_needed_to_retire = float(money_needed_to_retire)
        except ValueError:
            print money_needed_to_retire, 'this is not a dollar amount please try again! :'
            continue
        hours_worked_in_year = raw_input('how many hours do you work in a year')
        try:
            hours_worked_in_year = float(hours_worked_in_year)
        except ValueError:
            print hours_worked_in_year, 'this is not a number please try again'
        else:
            break
    print "Your dream job is %s!" % said  # string formatting is
    print "Your desired hourly wage is %.2f" % (hourly_wage)
   # print "If you get 4 weeks vacation then your annual wage is $ %.2f " % (CalculateAnnualWage(hourly_wage,hours_worked_in_year))
    print('\x1b[6;30;42m' + "You will need %.2f years of savings to retire" + '\x1b[0m') % (CalculateRetirement(money_needed_to_retire,(CalculateAnnualWage(hourly_wage,hours_worked_in_year))))
    print('\033[94m' + "If you get 4 weeks vacation then your annual wage is $ %.2f " + '\033[94m') % (CalculateAnnualWage(hourly_wage, hours_worked_in_year))
   # elif not CalculateRetirement(money_needed_to_retire,(CalculateAnnualWage(hourly_wage,hours_worked_in_year))) %  == 0:
    #    print CalculateRetirement(money_needed_to_retire,(CalculateAnnualWage(hourly_wage,hours_worked_in_year))), 'You will save for an odd numbers of years'

def main():
    GetJobInfo()
if __name__ == '__main__':
    main()