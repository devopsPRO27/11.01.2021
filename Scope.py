x = 5
def add():
    global x
    print(f'x inside the func {x}')
    def adder():
        x=12
        x=x+5
        print(f'x inside the func 2  {x}')
    adder()
add()
print(f'x outside the func {x}')