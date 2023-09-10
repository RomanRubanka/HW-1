# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
#     print("You go to next tour")    

# else:
#     is_next = False
#     print("Try again")

# is_active = input("Is the user active? ")
# is_admin = input("Is the user administrator? ")
# is_permission = input("Does the user have access? ")

# if is_active == True:
#     access = True
# else:
#     access = False  


# if is_admin == True or False:  
#     access = True
#     print ("Go")



# if is_active  or is_permission == True:
#     access = True
#     print ("Go")
# else:
#     access == False

# if is_admin == True or False:  
#     access = True
#     print ("Go")


# is_admin = input("Is the user administrator? ")
# is_admin = str(is_admin)
    
# if is_admin ==  True:  
      
#     access = True
#     print ("Go")

# else: 
#     is_active = input("Is the user active? ")

#     if is_active == True:  
    
#         is_permission = input("Does the user have access? ")
    
#         if is_permission == True:
#             access = True  
#         print ("Go")
#     else: 
#         access = False 
#     print ("Break")
    
# else:
# access = False
# print ("Break")

# is_admin = input("Is the user administrator? ")
    
# if is_admin == True:  
#     access = True
#     print ("Go")
    
# else:
#     is_active = input("Is the user active? ")
    
#     is_permission = input("Does the user have access? ")
        
#     if is_active  and is_permission == True:
#         access = True
#         print ("Go")
#     else:    
#         access = False
#         print ("BREAK")

# is_admin = bool(input("Is the user administrator? "))
# is_active = bool(input("Is the user active? "))
# is_permission = bool(input("Does the user have access? "))
#   111111111
# if is_admin == True:  
#     access = True
#     print ("Go")
    
# else:
        
#     if is_active  and is_permission == True:
#         access = True
#         print ("Go")
#     else:    
#         access = False
#         print ("BREAK")
        
# work_experience = int(input("Enter your full work experience in years: "))
#####2222222
# if (work_experience > 1) and (work_experience <= 5) :
#     developer_type = "Middle"
#     print(developer_type)

# elif work_experience <= 1 :
#     developer_type = "Junior"
#     print(developer_type)

# else: developer_type = "Senior"
# print(developer_type)

# num = int(input("Введіть число: "))
#333333333
# if num > 0:
#     if num >= 100:
#         result = "Додатне більше 100"
#     else:
#         result = "Додатне менше 100"
# elif num < 0:
#     result = "Число від'ємне"
# else:
#     result = "Це ноль"

# print(result)

# num = int(input("Enter a number: "))
#444444444
# if num > 0:
#     if num % 2 == 1:
#         result = "Positive odd number" # непарні
#     else: result = "Positive even number"  # парні
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# print(result)

# import math
#5555555555
# a = int(input("Enter coefficient a: "))
# b = int(input("Enter coefficient b: "))
# c = int(input("Enter coefficient c: "))

# D = b ** 2 - 4 * a * c

# if D >= 0:
    
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
    
#     print ("x1=", x1),
#     print ("x2=", x2)
    
#     if D < 0:
#          x1 = False,
#          x2 = False
# else:
#     print("try again")
#66666666


# num = int(input("Enter an integer number: "))


# is_even = bool("even") if num % 2 == 0 else False


# print(is_even)


#77777777

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# v = 1
# while v <= num:
#     sum = v + sum

#     v = v + 1
    
# print(sum)

#88888888

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."

# search = "r"
# result = 0

# for search in message :
#     if search == "r":
#         result += 1
        
# print(result)
        
# aliceQuote = "The best way to explain it is to do it."
# # с помощью цикла for посчитаем количество символов (с пробелами) в строке
# # зададим счетчик
# count = 0
# # будем посимвольно обходить весь текст
# for letter in aliceQuote:
#     # на каждой новой итерации: 
#     # в переменной letter будет храниться следующий символ предложения;
#     # увеличиваем счетчик на 1;    
#     count += 1

# print(count)

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."

# search = "r"
# result = 0

# for search_r in message :
#     if search_r == "r":
#         result += 1
        
# print(result)

# 99999
# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# if first < second:
#     gcd = first
# else:
#     gcd = second
    
#     while  gcd :
#         if ((first / gcd) - (first // gcd))  or ((second / gcd) - (second // gcd)):
    
#             gcd = gcd - 1
            
#             print (gcd)
#         else: 
#            # print (gcd)
#             break

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# if first < second:
#     gcd = first
# else:
#     gcd = second
    
# while first % gcd != 0 or second % gcd != 0:
    
#             gcd = gcd - 1
            
    # 10000000
    
# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num != 0:
#     repeat = int(input("Це ціле число? "))
#     for i in range (repeat) :
#         sum = sum + repeat
#     print(num)
#     num = int(input("Enter integer (0 for output): "))
    
# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num != 0 :
#     repeat = 0
#     for i in range (num + 1) :
#         sum = sum + i
#     repeat = repeat + sum
    
#     print(repeat)
#     num = int(input("Enter integer (0 for output): "))

    
    #111111111
    
# sum = 0   
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     repeat = 0
#     for i in range (num + 1) :
#         sum = sum + i
#     repeat = repeat + sum
    
#     print(repeat)
    
  # 122222222222  
  
# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     repeat = 0
#     for i in range(num + 1):
#         if i % 2 == 1:
#             continue
#         sum = sum + i
#     repeat = repeat + sum

#     print(repeat)
    
# 13333333
# message = input("Enter a message:  ")
# offset = int(input("Enter the offset:  "))
# encoded_message = ""
# for ch in message:
#     if ch.isalpha():
#         if ch.islower():
#             pos = ord(ch) - ord('a') 
#             pos = (pos + offset) % 26 
#             new_char = chr(pos + ord('a'))
#             encoded_message += new_char
#         else:
#             pos = ord(ch) - ord('A')
#             pos = (pos + offset) % 26
#             new_char = chr(pos + ord('A'))
#             encoded_message += new_char
#     else:
#         encoded_message += ch
        
# print(encoded_message)
    
# Spwwz xj wteewp qctpyod!      'Spwwz xj wteewp qctpyod!' 

# 144444444444
# try:
#     num = int(input("Введіть розмір команди: "))
#     award = 10000
#     bonus_for_person = award / num
# except ValueError:
#     print("Ви ввели не число!")
# except ZeroDivisionError:
#     print("Ви ввели нуль учасників!")
# else:
#     print(f"Нагорода кожному учаснику {bonus_for_person} золота!")
# finally:
#     print("До побачення!")

# pool = 1000 # SMS
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity        #розмір пакета
# except ZeroDivisionError:
#     print('Divide by zero completed!')
# finally:
#     print("Good by")

# 15555555555

# result = None   # підсумк результат
# operand = None   # зберігпає поточне число
# operator = None  # +-*/
# wait_for_number = True  #що очікують на вводі оператор чи операнд    
# result = 0
# while True:
#     char = input ( ">>>" )
#     if char == "=":
#         print ( f'Result: {result}')
#         break
#     elif wait_for_number:
#         try:
#             operand = int(char)
#             wait_for_number = False
#         except ValueError:
#             print  (f'{char} is not a number. Try again.' )
#             continue
#     else:
#         if char not in ('+','-','/','*'):
#             print(f'{char} is not “+” or “-” or “/” or “*”. Try again')
#             continue
#         operator = char
#         wait_for_number = True
#         if operator == '+':
#             result += operand
#         elif operator == '-':
#             result -= operand
#         elif operator == '*':
#             result *=operand
#         elif operator == '/':
#             if operand == 0:
#                 print ('ZeroDivisionError')
#                 continue
#             result /= operand
#     print (f' {result}')
        
        
        
      #  1555555
      

# operand = None   # зберігпає поточне число
# operator = None  # +-*/
# wait_for_number = True  #що очікують на вводі оператор чи операнд    
# result = None
# while True:
#     char = input ( ">>>" )
#     if char == "=":
#         print (f'Result: {result}')
#         break
#     if wait_for_number:
#         try:
#             operand = int(char)
#             wait_for_number = False
#         except ValueError:
#             print  (f'{char} is not a number. Try again.' )
#             continue
#         if result is None:
#             result = operand
#         else:
#             if operator == '+':
#                 result += operand
#             elif operator == '-':
#                 result -= operand
#             elif operator == '*':
#                 result *=operand
#             elif operator == '/':
#                 if operand == 0:
#                     print ('ZeroDivisionError')
#                 continue
#             result /= operand
#     else:
#         if char in ('+','-','/','*'):
#             operator = char
#         else:
#             operator = None
#         if operator is None:
#             print(f'{char} is not “+” or “-” or “/” or “*”. Try again')
#         else:
#             wait_for_number = True
        
#     print (f' {result}')
    
# 1515151515
operand = None   # зберігпає поточне число
operator = None  # +-*/
wait_for_number = True  #що очікують на вводі оператор чи операнд
result = None
while True:
    char = input( '>>>' )
    if char == '=':
        print(f'Result: {result}')
        break
    if wait_for_number:
        try:
            operand = int(char)
            wait_for_number = False
        except ValueError:
            print  (f'{char} is not a number. Try again.' )
            continue
        if result is None:
            result = operand
        else:
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *=operand
            elif operator == '/':
                if operand == 0:
                    print ('ZeroDivisionError')
                    continue
                result /= operand
    else:
        if char in ('+','-','/','*'):
            operator = char
        else:
            operator = None
        if operator is None:
            print(f'{char} is not “+” or “-” or “/” or “*”. Try again')
        else:
            wait_for_number = True
            
    print (f' {result}')
    
#     Code output:
#  2
# 3 is not “+” or “-” or “/” or “*”. Try again
#  2
#  2
#  1
#  1
#  11
#  11
#  22
# Result: 22

#Finish DZ 2-15