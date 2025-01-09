from prac_plunomial import polynomial 
      
def main():
    a=polynomial('x',2,[2,2,7])
    print(f'a is a polynomial :{a}')
    b=polynomial('x',2,[2,4,5])
    print(f'b is a polunomaial:{b}')
    print()
    print(f'Are a and b two  polynomial equal:')
    print(f' {polynomial.compare(a,b)}')
    print()
    r1=a * b
    print(f'multiplying two polynomials \n a*b: {r1}')
    print()
    r=a+b
    print(f'sum of two polynomial = \n a+b:{r}')
    print()
    c=polynomial('y',2,[3,2,8])
    print(f'c={c},{c.var}=2:\nevaluating c at {c.var}=2  Ans={a.evaluate(2)}')

if __name__=='__main__':
    main()