from MainPackage import main_script as main               #чтобы импортировать из скрипта, укажем имя папки. Можем через as приддумать псевдоним и через него обращаться
from MainPackage.SubPackage.subscript import *              #чтобы импортировать subscript, перейдем по папке. Все функции можно импортировать звездочкой (import *)


main.hello_main()                                   #теперь можем образаться к нему не через main_script а просто main
hello_subscript()
hello_indeed()

