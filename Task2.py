#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

inputNumber = input('Введите число: ')

print(f'Введенное число: {inputNumber}')

if inputNumber.isdigit() == True:
    product = 1
    productList = []
    for i in range(1, int(inputNumber) + 1):
        product *= i
        productList.append(product)
    print(productList)
