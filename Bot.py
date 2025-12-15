cache = {}
def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact

def oprMatrix(n):
    '''This function returns a matix of all the possible combinations of the operators'''
    opr = ['+', '-', '*', '/', '**', '%']
    oprCB_case = 4*(6**(n-2))
    oprCB = {}
    oprCB[1] = (['+']*(oprCB_case//2) + ['-']*int(oprCB_case//2))
    oprCB[2] = (['==+']*(oprCB_case//4) + ['==-']*(oprCB_case//4))*(2)
    for i in range(3,n+1):
        oprCB[i] = []
        for j in opr :
            oprCB[i] += ([j]*int(6**(n-i)))
        oprCB[i] *= (4*(6**(i-3)))
    for k in range(3,n+1):
        for c in oprCB :
            if c == k :
                temp = oprCB[c].copy()
                oprCB[c] += oprCB[2]
                oprCB[2] += temp
            elif c != 2 :
                oprCB[c] += oprCB[c]
    return oprCB

def numMatrix(L):
    '''This function returns a matix of all the possible combinations of the numbers'''
    n = len(L)
    numCB = {1:[]}
    fn = factorial(n)
    for k in L:
        numCB[1] += [k]*int(fn/n)
    for i in range(2,n+1):
        numCB[i] = []
        block = fn//factorial(n-(i-1))
        j = 1
        while j <= block:
            temp = L[:]
            for q in range(1,i):
                temp.remove(numCB[q][(j-1)*factorial(n-(i-1))])
            for m in temp:
                numCB[i] += [m]*(factorial(n-i))
            j += 1
    return numCB
                
def transpose(d):
    '''This function returns transpose of matrix 'd' in a list 'arrs' '''
    arrs = []
    for i in range(len(d[1])):
        arr = []
        for j in d :
            arr += [d[j][i]]
        if arr not in arrs :
            if arr.count('**') > 1 :
                for i in range(len(arr)-1):
                    if arr[i] == arr[i+1] == '**' :
                        break
                else :
                    arrs += [arr]
            else:
                arrs += [arr]
    return arrs

def statement(L):
    '''This function returns all the possible combinations of combined operators and numbers'''
    ln = len(L)
    if ln in cache :
        opr_arr = cache[ln]
    else :
        opr_arr = transpose(oprMatrix(ln))
        cache[ln] = opr_arr
    num_arr = transpose(numMatrix(L))
    statements = []
    for n in num_arr:
        for o in opr_arr:
            stmnt = ''
            for i in range(len(n)):
                stmnt += o[i]
                stmnt += str(n[i])
            statements += [stmnt]
    return statements

def choose(d):
    '''This function returns the statement with max points'''
    max = [0]
    i = 1
    for s in d:
        if eval(s):
            val = abs(eval(s.split('==')[0]))
            if val > max[0]:
                max = [val,s]
    if max == [0]:
        return False
    else:
        return max
