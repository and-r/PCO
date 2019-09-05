#coding: utf-8
import sys
import pcocore

#----COMPRESSION----
if len(sys.argv)<=1:
    Filesourcename=input("Please enter name of the file to compress :")
else:
    Filesourcename=sys.argv[1]
if len(Filesourcename)==0:
    print("File to compress is not given.")
    quit()
Filedestname=Filesourcename[:]
Filedestname+=".pco"
try:
    with open(Filesourcename,'rb') as Filesourceunpacked:
        Filedata=Filesourceunpacked.read()
except:
    print("Cannot open",Filesourcename)
    quit()
if len(Filedata) < 4:
    print("File is too short to deal with.")
    quit()
print("compression...")
Packedbytecount=pcocore.Compress(Filedata,Filedestname)
print("Succesfully written",Filedestname+", size =",Packedbytecount,"bytes")
