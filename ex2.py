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

#через * (variable length args)
def third_addr_function(*args):
    total = 0
    for n in args:
        total = total + n
    print(total)
third_addr_function(42,2,41,2.88)

# xs = [1, 2, 3]
# ss = ','.join(str(x) for x in xs) result -> '1,2,3'


"""
line = "switchport trunk allowed vlan 10,20,30"
vlans = line.split()[-1].split(",")
line2 = 'switchport trunk allowed vlan ' + ','.join(x for x in vlans)

"""


# использование kwargs 
# kwargs - использование **, что означает несколько аргументов, например значение и тип



def total_fruits(**kwargs):
    print(kwargs, type(kwargs))


total_fruits(banana=5, mango=7, apple=8)

def  print_my_args(**kwargs):
    for key,value in kwargs.items():
        print(f'The arg {key} was passed into the function with a value of {value}')
print_my_args(name="ivan", job="field engineer")

