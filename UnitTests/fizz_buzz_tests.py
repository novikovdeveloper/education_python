import unittest
import fizz_buz          #импортируем библиотеку, которую будем тестировать


class FizzBuzzTests(unittest.TestCase):      #создадим класс для тестирования
    #определим тестировочные случаи, методы, которые будут исполняться тест-раннером.И проверим поведение программы
    
    def test_fizz(self):
        number = 6 
        
        result = test_fizz.get_reply(number)  #передаем число из ф-ии в прошлом файле
        
        self.assertEqual(result, 'Fizz' )   #assertEqual-проверка ожидаемого результата,2й арг-то что мы ожидаем,1й-актуальный 
        
    
    def test_buzz(self):
        number = 10 
        
        result = test_buzz.get_reply(number)
        
        self.assertEqual(result, 'Buzz' )
        
    
    def test_fizzbuzz(self):
        number = 15
        
        result = test_fizzbuzz.get_reply(number)
        
        self.assertEqual(result, 'Fizz' )
        
        
        
if __name__ == '__main__':       #если скрипт запущен напрямую
    unittest.main()              #внутри этой конструкции будут прогонятся тесты, которые мы написали