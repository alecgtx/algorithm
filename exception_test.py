def num():
    a=int(input('input a : '))
    b=int(input('input b : '))
    return a, b

def func(a,b):
    add = a+b
    multi = a*b
    devi = a/b
    return add, multi, devi

if __name__=='__main__':
    try:
        a, b=num()
        add,_,_=func(a,b)
        _,multi,_=func(a,b)
        _,_,devi=func(a,b)

    except ZeroDivisionError:
        print('can not devide by zero')
        devi=func(a,1)
        pass
    finally:
        print(add, multi, devi)
pass
