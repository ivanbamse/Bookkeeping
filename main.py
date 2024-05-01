import application as app
from art import tprint
from datetime import date

if __name__ == '__main__':
    tprint("Bookkeeping", font="block", chr_ignore=True)
    tprint(app.people.get_employees())
    tprint(app.salary.calculate_salary())
    print(f"Today is: {date.today()}")


