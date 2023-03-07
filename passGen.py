import random as rand

def getChar_():
    symbs=['!','.','@','#','$','%','^','&','*','`','~','_','-','+','=']
    
    x = rand.randint(1,22)
    if rand.randint(1,66)>x:
        return chr(rand.randint(97, 122)) #common
    elif rand.randint(-2, 1) == 0:
        return symbs[rand.randint(0, len(symbs)-1)]
    elif rand.randint(-33, 22)<x:
        return chr(rand.randint(65, 90)) #caps

#      pass length(int), excluded chars(Str), if you want numbers or not (Bool)
def makePass(size, excluded, numsIncl):
    symb=['!','.','@','#','$','%','^','&','*','`','~','_','-','+','=']
    psw = ""; temp = ''
    if numsIncl == True:
        for v in range(size):
            temp = getChar_() 
            if temp != None and temp not in excluded:
                psw+=temp
                if rand.randint(0, 8) == rand.randint(3, 8):
                    psw+=str(rand.randint(0, 9))
    elif numsIncl == False:
        for v in range(size):
            temp = getChar_()
            if temp != None and temp not in excluded:
                psw+=temp
    psw = psw.replace(psw[-1], symb[rand.randint(0, len(symb)-1)])
    print(len(psw))
    return psw

passLength = 0;        exclusions_ = "";       numbersOrNot = ""

passLength = int(input("Enter password length :"))
exclusions_ = input("Enter chars you don't want :")
y = (input("Do you want numbers (True/False)?"))

if y == "True" or y =="true" or y=='t' or y=='T':
    numbersOrNot = True
else:
    numbersOrNot = False

print(makePass(passLength, exclusions_, numbersOrNot))