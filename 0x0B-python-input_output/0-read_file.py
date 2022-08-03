!/usr/bin/python3
""" This is a python fuction
that read a file """

def read_file(filename=""):
   
    with open('filename','w',encoding="utf-8") as fw:
            fw.write('hello world !')
            fw.close()
    with open('filename','r', encoding="utf-8") as fr:
            print(fr.read())
            fr.close()

read_file()
