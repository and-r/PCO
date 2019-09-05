#coding: utf-8
from pcocore import *
"""this file checks if decoding function gives the same N an L parameters as from the input for the coding function"""
for irep in range(1,17):
    if irep ==1:
        print("single sequence")
        for ilen in range(1,129):
            print("input N,L:",irep,ilen,"output:",end=' ')
            Codedbyte = Codingfunc(irep,ilen)
            print("C=",Codedbyte,end='')
            Tpl=Decodingfunc(Codedbyte)
            print(" N,L=",Tpl,Tpl==(irep,ilen))

    else:
        if irep ==2:
            print("multiple sequence")
        for ilen in range(1,9):
            print("input N,L:",irep,ilen,"output:",end=' ')
            Codedbyte = Codingfunc(irep,ilen)
            print("C=",Codedbyte,end='')
            Tpl=Decodingfunc(Codedbyte)
            print(" N,L=",Tpl,Tpl==(irep,ilen))        
