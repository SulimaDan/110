# def evaluate_expression(expression):

#     operations = ['+', '-', '*', '/']

#     for op in operations:
#         if op in expression:
#             left, right = expression.split(op)
            
#             left = float(left)
#             right = float(right)
            

#             if op == '+':
#                 return left + right
#             elif op == '-':
#                 return left - right
#             elif op == '*':
#                 return left * right
#             elif op == '/':
#                 return left / right

# input_expression = input("Введіть арифметичний вираз (наприклад, 23+12): ")

# result = evaluate_expression(input_expression)

# print("Результат:", result)


import random

list_size = 20  
random_list = [random.randint(-10, 10) for _ in range(list_size)]

min_element = min(random_list)
max_element = max(random_list)

negative_count = sum(1 for x in random_list if x < 0)
positive_count = sum(1 for x in random_list if x > 0)
zero_count = sum(1 for x in random_list if x == 0)


print("Згенерований список:", random_list)
print("Мінімальний елемент:", min_element)
print("Максимальний елемент:", max_element)
print("Кількість від'ємних елементів:", negative_count)
print("Кількість додатних елементів:", positive_count)
print("Кількість нулів:", zero_count)