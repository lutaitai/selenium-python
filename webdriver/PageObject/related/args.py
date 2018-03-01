def fun_arges1(arges):
    print("arges is %s" %arges)

def fun_arges2(arges1,arges2):
    print("arges1 is %s arges2 is %s" %(arges1,arges2))

def fun_var_args(*args):
    for value in args:
        print("args:",value)

fun_arges1('51zxw')
#fun_arges1('51zxw','python')

fun_arges2('51zxw','selenium')

fun_var_args('51zxw','python','selenium')