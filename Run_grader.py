import the4
import os
import time
import sys
start=time.time()
def main():
    with open("trees.txt") as file:
        data = file.read().split("\n")
    a=open("yourans.txt",'w')
    i=0
    for stree in (data):
        if stree!="":
            tree=eval(stree)
            answer = the4.chalchiuhtlicue(tree)
            i+=1
            a.write(str(answer)+"\n")
    a.close
main()
end=time.time()
os.system("./test_the4 "+str(end-start))
print "Your Code returned the answers in : "+str(end-start)
