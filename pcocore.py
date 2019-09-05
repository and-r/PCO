#coding: utf-8
import struct
Maxreplen=8 #max length of repeated sequence, bytes
Maxrepnum=16 #max number of repeated sequences
Maxnorepnum = 128  #max length of single sequence
Codingvarlen=1 #length of coding data, bytes 

def Codingfunc(N,L): #Coding:[N:number of repetitions, L:length of single/multiple sequence]
    """This is the version 'A' of coding function, that codes
    compression data into one byte as a signed char variable.
    Maximum length of repeates sequence: 8 bytes,
    maximum number of repeated sequences: 16,
    maximum length of non-repeated sequence: 128 bytes"""
    C=0     #int variable containing code number
    if N==1:
        C=L-1
    else:
        C=-(L-1)*16-(N-1)
    #print("C =",C,end=' ')
    
    return struct.pack('b',C)


def Decodingfunc(Codebyte):
    """This is the version 'A' of decoding function, 
    that decodes data coded by 'A' coding function"""
    Decodedint=struct.unpack('b',Codebyte)[0]
    N=0 #number of repetitions
    L=0 # length of single/multiple sequence
    if Decodedint >= 0: #single
        N = 1
        L = Decodedint+1
    else:   #multiple
        L = -Decodedint//16+1
        N = -Decodedint-(L-1)*16+1
    #print("N =",N," L =",L)
    return (N,L)

def Compress(filecontent,filedestname):
    global Maxreplen,Maxrepnum,Maxnorepnum,Codingvarlen
    Curcheckbegin=0  #seeker
    Endofcontent = False
    filelen=len(filecontent)
    if filelen < 4: #content is too short to deal with
        return 0
    destfile=open(filedestname,'wb')
    #print('---start of content analyze---\n')

    while 1:                                                                #LOOP 0
        Coding = [0,0] #[0- no coding,0 - sequence length
        i=Curcheckbegin
        while i < Curcheckbegin+Maxnorepnum:         #LOOP 1
            if i >= filelen-1:  #end of content encountered
                Endofcontent = True
                if Curcheckbegin<filelen:     #coding of single sequence at the end of content
                    Coding = [1,i+1-Curcheckbegin] 
                    #print("final single sequence, i=",i,"Coding =",Coding)
                    Codedsequence=Codingfunc(*Coding)+filecontent[Curcheckbegin:]     #asterisk unpacks sequence into list of arguments
                    destfile.write(Codedsequence)
                #print("end of content at i=",i)
                break
            else:
                i+=1
                for j in range (1,Maxreplen+1):                                #LOOP 2
                    if i-Curcheckbegin+1 >=j*2:
                        nonrep=0    #number of bytes not repeated
                        repcount=0      #counter of sequence repetitions
                        while filecontent[i-(j-1):i+1] == filecontent[i-(j-1)-j:i+1-j] and repcount < Maxrepnum-1:     #LOOP 3
                            repcount+=1
                            if Coding[0] == 0:            
                                nonrep=(i-Curcheckbegin+1)-j*2    #number of bytes to be coded as single sequence
                                if nonrep > 0:      #single sequence to be coded
                                    Coding=[1,nonrep]   
                                    #print('single sequence, i=',i,'Coding=',Coding)
                                    Codedsequence=Codingfunc(*Coding)+filecontent[Curcheckbegin:i+1-j*2]
                                    destfile.write(Codedsequence)
                                    Curcheckbegin+=nonrep
                            Coding = [(i-Curcheckbegin+1)//j,j]  #[number of repeats encountered up to this loop cycle(including),sequence length]
                            i+=j
                            if i >= filelen:  #end of content encountered
                                Endofcontent=True
                                break       # from LOOP 3
       
                        if Coding[0] > 1:
                          #print('multiple sequence, i=',i,'Coding=',Coding)
                          Codedsequence=Codingfunc(*Coding)+filecontent[Curcheckbegin:Curcheckbegin+Coding[1]]
                          destfile.write(Codedsequence)
                          Curcheckbegin += Coding[0]*Coding[1]
                          i=Curcheckbegin
                          Coding = [0,0]    #reset
                          break     #from LOOP 2  
                        if Endofcontent==True:
                            break   #from LOOP 2
                            
                
        if Endofcontent is True:
            break
        else:
            #single sequence of maximum length to be coded
            Coding=[1,Maxnorepnum]
            #print("max length single sequence, i=",i,"Coding =",Coding)
            Codedsequence=Codingfunc(*Coding)+filecontent[Curcheckbegin:Curcheckbegin+Maxnorepnum]
            destfile.write(Codedsequence)
            Curcheckbegin+=Maxnorepnum 
    destfilelength=destfile.tell()  
    destfile.close()
    return destfilelength

def Decompress(filesourcename,filetargetname):
    sourcefile=open(filesourcename,'rb')
    sourcedata=sourcefile.read()
    targetfile = open(filetargetname,'wb')
    """print("sourcedata[0]=",sourcedata[0:1])
    print(type(sourcedata))
    print(type(sourcedata[0:1]))"""
    extractedbytes=0
    i=0
    while i<len(sourcedata):
        N,L=Decodingfunc(sourcedata[i:i+1])    #function returns tuple
        #print("read N,L:",N,L)
        for j in range(0,N):
            #extractedbytes+=sourcedata[i+1:i+1+L]
            extractedbytes+=targetfile.write(sourcedata[i+1:i+1+L])
        i+=L+1
    sourcefile.close()
    targetfile.close()
    return extractedbytes
        
    

    

