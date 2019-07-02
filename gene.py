from os import system
from random import randint
from time import sleep as s

cls = lambda: system('cls')

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

print("Only use letters and spaces")
target = input("Target: ").upper()
print("Only use positive whole numbers")
size = int(input("Population size: "))
print("Only use positive numbers between 1 and 0")
mRate = int(float(input("Mutation rate: "))*100)
print("Only use positive whole numbers")
tests2run = int(input("How many tests?"))

tests = []

for T in range(0,tests2run):

    pop = []

    generation = 0
    
    #generate population
    for i in range(0,size):
        DNA = ""
        for j in range(0,len(target)):
            DNA+=alph[randint(0,26)]
        pop += [DNA]

    #test loop
    while True:
        matingPool = []

        best = 0
        bestI = 0
        
        #Score and generate mating pool
        for i in range(0,size):
            DNA = pop[i]
            score = 0
            for i in range(0,len(DNA)):
                score+= DNA[i] == target[i]
            matingPool+= [DNA] * (score*score+1)

            if score >= best:
                best = score
                bestI = i
        
        cls()
        print("Test: "+str(T)+" Generation: "+str(generation)+"\nBest: "+pop[i])
            

        if pop[i] == target:
            break
        pop = []

        #generate new population (Cross breeding)
        for i in range(0,size):
            c1 = matingPool[randint(0,len(matingPool)-1)]
            c2 = matingPool[randint(0,len(matingPool)-1)]
            c3 = ""
            for i in range(0,len(DNA)):
                c3+= ((c1[i] if randint(0,1) == 1 else c2[i]) if randint(0,100) < (100-mRate) else alph[randint(0,26)])
            pop+=[c3]

        generation+= 1

    tests+= [generation]

    print("Test "+str(T)+" Solved at generation "+str(generation)+" average is "+str(sum(tests)/len(tests)))
    if tests2run <= 10: s(0.75)
cls()
print("Solved a "+str(len(target))+" character string "+target+" in an average of "+str(sum(tests)/len(tests))+" generations.")

