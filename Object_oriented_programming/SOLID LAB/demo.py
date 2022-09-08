                ####SOLID PRINCIPLES####

#валидни за всеки обекто ориентиран език
#S# Single Responsibility
#O# Open/Closed
#L# Liskov substitution
#I# Interface Segregation
#D# Dependency Inversion

#на Ниво цялостна структура на our application#
#правят кода по лесен за поддръжка , абстрактен и лесен за четене и разбиране
####S#### Single Responsibility
#всеки клас или метод трябва да прави точно определено нещо

def my_sum(numbers):    # няма single responsibility
    the_sum = sum(numbers)
    print(the_sum)

####O#### Open/Closed
#всеки компонент must be open for extension but close to modification
#its achieved with:
            #Abstaction
            #Mix-ins
            #Monkey-Patching
            #Generic functions(Using overrloading)

#идеята е да можем да променим логиката за нашия код БЕЗ ДА СЕ НАЛАГА
#да променяме РОДИТЕЛСКИЯ КЛАС!

####Liskov Substitution####
#Всеки наследник трябва да се държи като родителя.
#Design Smell = VIOLATIONS:
#If the code is checking the type of class
#Overriden methods change their behaviour
#Override a method of the superclass by an empty method
#Base class depends on its subtypes

###Interface Segregation###
#Един клас не трябва да има методи които не използва
#по добре е да направим много класове с по един метод
#отколкото един клас с много методи !
#в един клас трябва да има точно методите които му трябват!

###Dependency Inversion###
#Не трябва да разчитаме на конкретики а на Абстракции