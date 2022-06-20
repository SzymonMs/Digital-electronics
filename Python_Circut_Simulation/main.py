def NOT(a):
    return not(a)
def AND(a,b):
    return a and b
def OR(a,b):
    return a or b
def NAND(a,b):
    return NOT(AND(a,b))
def NOR(a,b):
    return NOT(OR(a,b))
def XOR(a,b):
    return AND(OR(a,b),NOT(AND(a,b)))
def XNOR(a,b):
    return NOT(XOR(a,b))
def AND3(a,b,c):
    return AND(AND(a,b),c)
def OR3(a,b,c):
    return OR(OR(a,b),c)
def NAND3(a,b,c):
    return NAND(NAND(a,b),c)

if __name__ == '__main__':
    # y = a'b'c+a'bc'+ab'c'
    a = [True,False]
    b = [True,False]
    c = [True,False]
    y = []
    y21 = []
    for aa in a:
        for bb in b:
            for cc in c:
                y1 =  AND(AND(NOT(aa),NOT(bb)),cc)
                y2 =  AND(AND(NOT(aa),NOT(cc)),bb)
                y3 =  AND(AND(NOT(bb),NOT(cc)),aa)
                y.append(OR(OR(y1,y2),y3))
    for aa in a:
        for bb in b:
            for cc in c:
                y1 = AND3(NOT(aa),NOT(bb),cc)
                y2 = AND3(NOT(aa),NOT(cc),bb)
                y3 = AND3(NOT(bb),NOT(cc),aa)
                y21.append(OR3(y1,y2,y3))
    print(y)
    print(y21)
