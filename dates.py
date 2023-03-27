import re

class GregDate:
    '''
    Класс с функциями для работы с Григорианскими датами
    '''

    def __init__(self, str, type = 0):
        l = str.split('.')
        self.day = int(l[0])
        self.month = int(l[1])
        self.year = type*100 + int(l[2])


    def is_leap_year(self, year = 0):
        '''
        Проверяет високосный год или нет
        '''

        if year == 0:
            year = self.year

        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False


    def format_number(self, num):
        if num < 10:
            return "0" + str(num)
        else:
            return str(num)


    def to_string(self):
        s = self.format_number(self.day)+ "." + self.format_number(self.month) + "." + str(self.year)
        return s

    def count_days_in_previous_year(self):
        '''
        Считает количество полных дней в прошлом году
        '''
        len_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
       
        if self.is_leap_year(self.year - 1):
            len_months[1] = 29
        return sum(len_months)

    def to_number(self):
        '''
        Переводит дату в порядковое число от начала года
        '''
        len_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
       
        if self.is_leap_year():
            len_months[1] = 29
        
        sum = 0
        for i in range(0, self.month - 1):
            sum += len_months[i]
        sum += self.day
        return sum

class ChineseDate:
    '''
    Класс, пполучающий основные характеристики китайской даты
    '''

    dates19 = ['31.01.00', '19.02.01', '08.02.02', '29.01.03', '16.02.04', '04.02.05', '25.01.06', '13.02.07', '02.02.08', '22.01.09', '10.02.10', '30.01.11', '18.02.12', '06.02.13', '26.01.14', '14.02.15', '03.02.16', '23.01.17', '11.02.18', '01.02.19', '20.02.20', '08.02.21', '28.01.22', '16.02.23', '05.02.24', '24.01.25', '13.02.26', '02.02.27', '23.01.28', '10.02.29', '30.01.30', '17.02.31', '06.02.32', '26.01.33', '14.02.34', '04.02.35', '24.01.36', '11.02.37', '31.01.38', '19.02.39', '08.02.40', '27.01.41', '15.02.42', '05.02.43', '25.01.44', '13.02.45', '02.02.46', '22.01.47', '10.02.48', '29.01.49', '17.02.50', '06.02.51', '27.01.52', '14.02.53', '03.02.54', '24.01.55', '12.02.56', '31.01.57', '18.02.58', '08.02.59', '28.01.60', '15.02.61', '05.02.62', '25.01.63', '13.02.64', '02.02.65', '21.01.66', '09.02.67', '30.01.68', '17.02.69', '06.02.70', '27.01.71', '15.02.72', '03.02.73', '23.01.74', '11.02.75', '31.01.76', '18.02.77', '07.02.78', '28.01.79', '16.02.80', '05.02.81', '25.01.82', '13.02.83', '02.02.84', '20.02.85', '09.02.86', '29.01.87', '17.02.88', '06.02.89', '27.01.90', '15.02.91', '04.02.92', '23.01.93', '10.02.94', '31.01.95', '19.02.96', '07.02.97', '28.01.98', '16.02.99']
    dates20 = ['05.02.00', '24.01.01', '12.02.02', '01.02.03', '22.01.04', '09.02.05', '29.01.06', '18.02.07', '07.02.08', '26.01.09', '14.02.10', '03.02.11', '23.01.12', '10.02.13', '31.01.14', '19.02.15', '08.02.16', '28.01.17', '16.02.18', '05.02.19', '25.01.20', '12.02.21', '01.02.22', '22.01.23', '10.02.24', '29.01.25', '17.02.26', '06.02.27', '26.01.28', '13.02.29', '03.02.30', '23.01.31', '11.02.32', '31.01.33', '19.02.34', '08.02.35', '28.01.36', '15.02.37', '04.02.38', '24.01.39', '12.02.40', '01.02.41', '22.01.42', '10.02.43', '30.01.44', '17.02.45', '06.02.46', '26.01.47', '14.02.48', '02.02.49', '23.01.50', '11.02.51', '01.02.52', '19.02.53', '08.02.54', '28.01.55', '15.02.56', '04.02.57', '24.01.58', '12.02.59', '02.02.60', '21.01.61', '09.02.62', '29.01.63', '17.02.64', '05.02.65', '26.01.66', '14.02.67', '03.02.68', '23.01.69', '11.02.70', '31.01.71', '19.02.72', '07.02.73', '27.01.74', '15.02.75', '05.02.76', '24.01.77', '12.02.78', '02.02.79', '22.01.80', '09.02.81', '29.01.82', '17.02.83', '06.02.84', '26.01.85', '14.02.86', '03.02.87', '24.01.88', '10.02.89', '30.01.90', '18.02.91', '07.02.92', '27.01.93', '15.02.94', '05.02.95', '25.01.96', '12.02.97', '01.02.98', '21.01.99']
    

    def __init__(self, greg_date: GregDate):
        self.greg_date = greg_date
        self.ny_date = self.find_NY_date()
        self.set_year()
        self.set_day_and_month()

    def print_info(self):
        print("Григорианская дата: " + self.greg_date.to_string() + " " + str(self.greg_date.to_number()) )
        print("Китайский Новый год начался: " + self.ny_date.to_string() + " " + str(self.ny_date.to_number()) )
        print("")
        print("Цикл китайского года: " + str(self.year_cycle))
        print("Китайский год: " + str(self.year))
        print("Ветвь года: " + str(self.year_branch))
        print("Элемент года: " + str(self.year_element))
        print("")
        print("Китайский месяц: " + str(self.month))
        print("Китайский день: " + str(self.day))

    def set_year(self):
        year = self.ny_date.year
        self.year_cycle = (year + 2697) // 60 + 1
        self.year = (year + 2697) % 60
        self.year_branch = (year - 1924) % 12 + 1
        self.year_element = ((year - 1924) % 10) // 2 + 1


    def set_day_and_month (self):
        diff = (self.greg_date.to_number() - self.ny_date.to_number())
        if self.greg_date.year > self.ny_date.year or diff < 0:
            diff += self.greg_date.count_days_in_previous_year()
        div = diff // 59
        mod = diff % 59
        month = div * 2
        day = 0
        if mod > 29:
            month += 1
            day = mod - 29
        else:
            day = mod
        self.month = month + 1
        self.day = day + 1

    def find_NY_str(self, year):
        '''
        Ищет строку в списках с датами китайских НГ  по году
        '''
        if 1900 <= year < 2000 :
            type = 19
            y = year % 100
        elif 2000 <= year < 3000:
            type = 20
            y = year % 100
        else:
            raise BaseException("Ошибка! Года вне диапозона [1900; 3000) не переводим!")

        dates = self.dates19 if type == 19 else self.dates20
        ny_str = dates[y]
        return (ny_str, type)


    def find_NY_date(self):
        year = self.greg_date.year
        (ny_str, type) = self.find_NY_str(year)        
        ny = GregDate(ny_str, type).to_number()
        current = self.greg_date.to_number()

        if current < ny : # текущая дата раньше НГ, значит по китайскому календарю это еще прошлогодний год
            year -= 1
            (ny_str, type) = self.find_NY_str(year)
        
        return GregDate(ny_str, type)
