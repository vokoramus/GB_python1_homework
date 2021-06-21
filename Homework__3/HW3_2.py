''' 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.'''


def user_data(name, surname, year, city, email, phone):
    output_data = f"User: {surname} {name} from {city}, year of birth: {year}, email: {email}, phone number: {phone}"
    return output_data


print(user_data(name="Yuriy", surname="Sumarokov", year="1984", city="Saint-Petersburg", email="vokoramus01@ya.ru", phone="8-911-190-69-12",))

