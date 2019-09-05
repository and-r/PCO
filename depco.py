#coding: utf-8
import sys
import pcocore

#---DECOMPRESSION----
if len(sys.argv)<=1:
    Filesourcename=input("Please enter name of the file to extract :")
else:
    Filesourcename=sys.argv[1]
if len(Filesourcename)==0:
    print("File to extract is not given.")
    quit()
try:
    checkfileopen=open(Filesourcename,'rb')
    checkfileopen.close()
except:
    print("Cannot open",Filesourcename)
    quit()
print("extraction...")
if Filesourcename[-4:]==".pco":
    Filedestname=Filesourcename[:-4]
else:
    Filedestname=Filesourcename+".dpco"

Extractedbytes=pcocore.Decompress(Filesourcename,Filedestname)

print("Succesfully written",Filedestname)

