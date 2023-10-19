from datetime import date

from prettytable import PrettyTable

from application.salary import calculate_salary
from application.db.people import get_employees


def current_date():
   return print(date.today())

def income():
   x = PrettyTable()
   x.field_names = ["Ф.И.О.", "Доход", "Расход"]
   x.add_rows([["Иванов И.И.", 1000, 500], ["Петров П.П.", 2000, 700]])
   x.add_column("Остаток", [500, 1300])
   return print(x)
   

if __name__ == '__main__':
    c=calculate_salary()
    e=get_employees()
    print(f'Зарплата сотрудника {e[0]} равна {c}')
    print(f'Зарплата сотрудника {e[1]} равна {c*2}')
    current_date()
    income()
