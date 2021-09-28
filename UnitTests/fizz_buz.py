#Fiz_Buzz
#На вход подаются числа, если число делиться на 5 без остатка - buz, на 3 -fiz, если на 3 и 5 то fizbuz. Else пустая строка


def get_reply(number):
    if number%5==0 and number%3==0:
        return 'FizBuzz'
    elif number%3==0:
        return 'Fiz'
    elif number%5==0:
        return 'Buz'
    else:
        return ''
    
#В след файле напишим юнит-тест для этого кода
        