#!/usr/bin/env python
"""Demonstrates input."""

NUMBER_OF_WEEKS_IN_A_WORK_YEAR = 52
NUMBER_OF_WORK_HOURS_IN_A_WEEK = 40
HOURS_WORKED_IN_A_YEAR = 1920

def CalculateAnnualWage(hourly_rate=15.5, hours_worked=(NUMBER_OF_WEEKS_IN_A_WORK_YEAR * NUMBER_OF_WORK_HOURS_IN_A_WEEK)):
    return hourly_rate * hours_worked

def CalculateRetirement(money_needed_to_retire=100000,yearly_salary=20000):
    return money_needed_to_retire / yearly_salary


def GetPrompt(prompt):
    while True:
        said = raw_input(prompt)
        try: said = float(said)
        except ValueError:
            print said, "Please try again and enter a numberical value: "
        else:
            break







    print "Your desired hourly wage is %.2f" % (hourly_wage)
    print "If you get 4 weeks vacation then your annual wage is $ %.2f " % (CalculateAnnualWage(hourly_wage, hours_worked_in_year))
    print "You will need %.2f years of savings to retire" % (CalculateRetirement(money_needed_to_retire, (CalculateAnnualWage(hourly_wage, hours_worked_in_year))))

def Test():
    GetJobDescription()
    #print GetPrompt(Test())
    GetPrompt('What is your desired hourly rate: ')
    GetPrompt('How much savings do you need to retire: ')
    GetPrompt('How many hours do you work in a year: ')

def GetJobDescription():
    while True:
        dream_job = raw_input('What is your dream job: ')
        try: dream_job = str(dream_job)
        except ValueError:
            print dream_job, "Please try again"
        else:
            break
    print "Your dream job is %s!" % (dream_job)  # string formatting is

#GetPrompt()
#Test()
def main():
    Test()
    #GetJobInfo('boss')
    #CalculateRetirement()
    #CalculateAnnualWage()
if __name__ == '__main__':
    main()