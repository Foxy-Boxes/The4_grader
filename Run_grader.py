import the4
import os
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
os.system("./test_the4")
