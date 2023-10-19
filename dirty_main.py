from application.salary import *
from application.db.people import *
from main import *



if __name__ == '__main__':
    c=calculate_salary()
    e=get_employees()
    print(f'Зарплата сотрудника {e[0]} равна {c}')
    print(f'Зарплата сотрудника {e[1]} равна {c*2}')
    current_date()
    income()
