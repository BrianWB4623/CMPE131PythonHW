def my_steps(n):
    if(n>25 or n<1):
        raise ValueError("n should be >=1 and <=25")
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return my_steps(n - 1) + my_steps(n - 2)
