def fib(n):
    """Calculates the nth Fibonacci number"""
    a=1
    b=1
    c=1
    rc=0
    d=0
    rd=1
    if n >= 0:
        while n>0:
            if n%2!=0: #multiple matrix a with vector r
                tc = rc
                rc = rc*a + rd*c
                rd = tc*b + rd*d
            ta = a
            tb = b
            tc = c
            a = a*a + b*c
            b = ta*b + b*d
            c = c*ta + d*c
            d = tc*tb + d*d
            n >>=1
        return rc
    else:
        return ((-1)**((n*(-1))+1))*fib(n*(-1))
    
    
