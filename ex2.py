def my_addr_fucntion(num1,num2):
    print(num1 + num2)

my_addr_fucntion(7,2)

# Только два аргумента, попробуем пофиксить через loop
def second_addr_function(my_list):
    total = 0 
    for num in my_list:
        total = total + num 
    print (total)

second_addr_function([2,5,7,100])

#через loop