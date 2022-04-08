import re


class Bank:
    
    def __init__(self, valuta, name='Unkmown'):  #__init__ контруктор испольняет код по время создание обьека x = Bank('RUB')
        if valuta not in ( 'RUB', 'Com'):
            raise ValueError
        self.__money = 0.00 # __money инкапцуляция свойтво которое защищает и получает данные только из класса 
        self.valuta = valuta
        self.name = name
        
    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany
        
    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('Не достаточно средств')
            raise ValueError('Не достаточно средств')
        self.__money = self.__money - howmany   
        return howmany 
    
    def info(self):
        print(self.__money)
    
    def __del__ (self): # декруктор код работает во время удаление 
        print('Кошелек удален')
    
x = Bank('RUB')
y = Bank('Сом')
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))
x.info()
y.info()
