# def == definition
def calculate(a,b):
    print(a+b)
    return

calculate(2,4)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit? ')

i = 5

def f(arg=i):
    print(arg)

i = 6
f()