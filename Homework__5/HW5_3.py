'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''

salary_average, salary_sum = 0, 0
n, n_min = 0, 0
SALARY_MIN = 20000


with open("HW5_3_text.txt", 'r', encoding="utf-8") as f:
    for line in f.readlines():
        n += 1
        data = line.strip().split()
        surname = data[0]
        salary = int(data[1])
        salary_sum += salary
        if salary < SALARY_MIN:
            n_min += 1
            print(surname)
try:
    salary_average = salary_sum / n
    print(f"salary_average = {salary_average:.2f}", )
except ZeroDivisionError:
    print("There is no staff in your file")
