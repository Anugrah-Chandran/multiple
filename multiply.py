def multiple_of_numbers(x):
    product = 1
    for i in x:
        product = i*product
    return product

lst = eval(input("Enter the list of numbers: "))
print(multiple_of_numbers(lst))
