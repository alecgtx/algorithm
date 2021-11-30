import argparse

args=argparse.ArgumentParser()
args.add_argument('-x', required=True)
args.add_argument('-y', required=True)
args.add_argument('-z', required=True)
argvar=vars(args.parse_args())
pass


x,y,z=argvar()

def func(x,y,z):
    multi = x*y
    devi = y/z
    return multi, devi

if __name__=='__main__':
    while 1:
        try:
            x,y,z=argvar()
            multi,_=func(x,y)
            _,devi=func(y,z)

        except ZeroDivisionError:
            print('can not devide by zero')
            devi=func(y,1)
            pass

        finally:
            try:
                print('multiply = ', multi, 'devide = ', devi)

            except:
                pass
    
        

    

