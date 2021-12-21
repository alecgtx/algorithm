import argparse

args=argparse.ArgumentParser()
args.add_argument('-x', type=int, required=True)
args.add_argument('-y', type=int, required=True)
args.add_argument('-z', type=int, required=True)
argvar=vars(args.parse_args())
pass

def aVal(argvar):
    x=argvar.get('x')
    y=argvar.get('y')
    z=argvar.get('z')
    return x,y,z

if __name__=='__main__':
    try:
        
        x,y,z=aVal(argvar)
        multi=x*y
        devi=y/z
        print(multi,devi)

    except ZeroDivisionError:
        print('can not devide by zero')
        devi=y/1
        pass

    finally:
        try:
            print('multiply = ', multi, 'devide = ', devi)
        except:
            pass 
        

    

