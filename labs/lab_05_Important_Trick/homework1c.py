# !/usr/bin/env python
"""Demonstrates input."""
NUMBER_OF_WEEKS_IN_A_WORK_YEAR = 52
NUMBER_OF_WORK_HOURS_IN_A_WEEK = 40
HOURS_WORKED_IN_A_YEAR = 1920


def CalculateAnnualWage(hourly_rate=15.5,hours_worked=(NUMBER_OF_WEEKS_IN_A_WORK_YEAR * NUMBER_OF_WORK_HOURS_IN_A_WEEK)):
    return hourly_rate * hours_worked

def CalculateRetirement(money_needed_to_retire=100000, yearly_salary=20000):
    return money_needed_to_retire / yearly_salary

def GetPrompt(prompt):
    while True:
        said = raw_input(prompt)
        try: said = str(said)
        except ValueError:
            print said, "this is not a job description try again"
        else:
            break

def GetDreamJobInfo(dream_job, hourly_wage=10, money_needed_to_retire=10000, hours_worked_in_year=2000):
    while True:  # True/False are keywords.
        dream_job = raw_input('What is your dream job? ')
        hourly_wage = raw_input('What is your hourly rate ? ')
        money_needed_to_retire = raw_input('How much money do you need to retire? ')
        hours_worked_in_year = raw_input('How many hours do you work in a year? ')  # This was for teesting logic
        try:
            dream_job = str(hourly_wage)
        except ValueError:
            print dream_job, 'Please enter a job description! Please try again.'
        else:
            break
        try:
            hourly_wage = float(hourly_wage)
        except ValueError:
            print hourly_wage, 'is not a wage ! Please try again.'
        else:
            break
        try:
            money_needed_to_retire = float(money_needed_to_retire)
        except ValueError:
            print money_needed_to_retire, 'is not a dollar amount:  ! Please try again.'
        else:
            break
        try:
            hours_worked_in_year = float(hours_worked_in_year)
        except ValueError:
            print hours_worked_in_year, 'Please enter hours worked in a year ! Please try again.'
        else:
            break
    print "Your dream job is %s!" % (dream_job)  # string formatting is
    print "Your desired hourly wage is %.2f" % (hourly_wage)
    print "If you get 4 weeks vacation then your annual wage is $ %.2f " % (CalculateAnnualWage(hourly_wage, hours_worked_in_year))
    print "You will need %.2f years of savings to retire" % (CalculateRetirement(money_needed_to_retire, (CalculateAnnualWage(hourly_wage, hours_worked_in_year))))

def Test():
    GetPrompt('What is your dream job? : ')
    print GetPrompt()
    GetPrompt('What is your desired hourly rate: ')
    GetPrompt('How much savings do you need to retire: ')
    GetPrompt('How many hours do you work in a year: ')
    exit()

def main():
    GetDreamJobInfo(GetPrompt())
    #GetDreamJobInfo(Test())
    #Test()
    if __name__ == '__main__':
        main()