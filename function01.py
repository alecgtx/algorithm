def fun01():
    fun02() 
    return

def fun02():
    fun03()
    return

def fun03():
    return

if __name__ == '__main__':
    fun01()
    pass