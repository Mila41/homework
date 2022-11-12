# Зарплата сотрудника составляет salary руб
# Расходы на проживание превышают зарплату и составляют expenses руб в месяц
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Напишите скрип расчета суммы денег, которую необходимо взять в долг
# чтобы можно было прожить ближайший год (12 месяцев) в формате
# Необходимо взять в долг ххх.хх рублей
зп, расходы = 10000, 12000

salary = float(input('Ввведи ЗП '))
exp = float(input('Введи расход '))
month = [1,2,3,4,5,6,7,8,9,10,11,12]
exp_total = exp
if salary >= exp:
    print("Условия не верны")
else:
    for i in month:
        print(i)
        if i!=1:
            all_salary = salary * 1
            print(all_salary)
            exp = exp * 1.03
            exp_total = exp_total + exp
            print(exp_total)
    live = abs(all_salary - exp_total)
print("Необходимо занять ", round(live,2))            

