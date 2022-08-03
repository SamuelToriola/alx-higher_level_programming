!/usr/bin/python3
""" This is a python fuction
that read a file """

def read_file(filename=""):
   
    with open(filename.txt,'w', encoding="utf-8") as fw:
            fw.write('Something\n')
            fw.close()
            fr = open(filename.txt ,'r', encoding="utf-8")
            file = fr.read()
            print(file , end="")
            fr.close()
