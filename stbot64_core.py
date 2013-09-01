
###
# StBot Base 64 core lib revised
#
#       Filename: stbot64_core
#       Author:   StBot
#       Date:     June 18, 2013
#       Version:  1.0
#
###
# Revisions
#   FILE rewrite ON 6/18/13 - learning python it was ugly
#     6/18/13
#       1. better name scheem and documentation
#       2. Replced flag Names to make more sence for debuging. - Smarter type checking code can remove these
#       3. all inputs and outputs are standeredised as strings unless 
#        otherwise noted
#       4. Phased out the 'grouper' replaced with sliceing useing 'chunks' - No More Tuples = less loops!!
#     6/27/13  
#       1. inputvalidater seems to be compleate. implementing where needed.
#       2. working version 1.0!!
#     7\2\13
#       1. added None type for = in base_to_bin
###
# 
#       FIXME ln 196 The output on dec to hex has been changed to always return a list i prolly broke something  
# 
#       
#       
#       
#       
#       
#       
#
###


def inputvalidater(inputval, typecheck = 0):
    """takes the given input an checks it to make sure 
    there are an even number of charicters && changes types to strings
    it will not change values to string if the sending function requires a list.
    Type check codes are used to deturmine the rewuired type for the sending function
    TYPE CHECK CODES:: 0-String (default) 1-List"""
    
    if type(inputval) is str and typecheck == 0:          
        if len(inputval)%2 ==0:
            return True,inputval
    elif type(inputval) is list and typecheck == 0:
        inputval = ''.join(inputval)
        if len(inputval)%2 == 0:
            return True,inputval
    elif type(inputval) == str and typecheck == 1:
        return False, "ERROR"
    elif type(inputval) is list and typecheck ==1:
        for x in inputval:
            if type(x) is str:
                if len(x)%2 ==0:
                    returnval = True
            elif type(x) is int:
                if len(str(x))%2==0:
                    returnval = True
        return returnval, inputval
    return False, "ERROR"
    
    
    
    

def chunks(s,n):                                                                              
    """breaks strings of data into chunks of size n. output is a LIST """
    output = []
    for start in range(0, len(s), n):
         output.append(s[start:start+n])
    return output  # THIS OUTPUT IS A LIST

def hex_to_bin(hexinput):                                                                    
    """ converts a string of hex to a string of binary"""
    valid,hexinput = inputvalidater(hexinput)
    if hexinput == "ERROR":
        print "INVALID INPUT ID: Core 78"
        return None
    binoutput = []
    hex_bindict= {'0':"0000",
       '1':"0001",
       '2':"0010",
       '3':"0011",
       '4':"0100",
       '5':"0101",
       '6':"0110",
       '7':"0111",
       '8':"1000",
       '9':"1001",
       'a':"1010",
       'b':"1011",
       'c':"1100",
       'd':"1101",
       'e':"1110",
       'f':"1111"}
    for x in hexinput:
        binoutput.append(hex_bindict[x])
    return ''.join(binoutput)

def bin_to_hex(bininput):                                                                    
    """ converts a string of binary to a string of hex"""
    binlist =[]
    hexoutput = []
    bin_hex_dict= {'0000':'0',
           "0001":'1',
           "0010":'2',
           "0011":'3',
           "0100":'4',
           "0101":'5',
           "0110":'6',
           "0111":'7',
           "1000":'8',
           "1001":'9',
           "1010":'a',
           "1011":'b',
           "1100":'c',
           "1101":'d',
           "1110":'e',
           "1111":'f'}
    binlist = chunks(bininput,4)
    for x in binlist:
        hexoutput.append(bin_hex_dict[x])
    return ''.join(hexoutput)
    
def bin_to_base(binaryinput):                                                                           
    """ converts a string of binary to a string of base64"""
    basedict= {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H' ,
               8:'I', 9:'J', 10:'K' ,11:'L' ,12:'M' ,13:'N' ,14:'O' ,
               15:'P' ,16:'Q' ,17:'R' ,18:'S' ,19:'T' ,20:'U', 21:'V' ,
               22:'W' ,23:'X' ,24:'Y' ,25:'Z' ,26: 'a',27:'b' ,28:'c' ,
               29:'d' ,30:'e' ,31:'f' ,32:'g' ,33:'h' ,34:'i' ,35:'j' ,
               36:'k' ,37:'l' ,38:'m' ,39:'n' ,40:'o' ,41:'p' ,42:'q' ,
               43:'r' ,44:'s' ,45:'t' ,46:'u' ,47:'v' ,48:'w' ,49:'x' ,
               50:'y' ,51:'z' ,52:'0' ,53:'1' ,54:'2' ,55:'3' ,56:'4' ,
               57:'5' ,58:'6' ,59:'7' ,60:'8' ,61:'9' ,62:'+' ,63:'/' }
    binarylist = chunks(binaryinput,6)
    baselist = []
    for x in binarylist:
        exp=5
        total =0
        for y in x:
            total += int(y)*2**exp
            exp -= 1
        baselist.append(basedict[total])
    return ''.join(baselist)

def base_to_bin(baseinput):                                                                             
    """ converts a string of base64 to a string of binary"""
    basebindict = {'A':0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8
                 ,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16
                 ,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24
                 ,'Z':25,'a':26,'b':27,'c':28,'d':29,'e':30,'f':31,'g':32
                 ,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40
                 ,'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48
                 ,'x':49,'y':50,'z':51,'0':52,'1':53,'2':54,'3':55,'4':56
                 ,'5':57,'6':58,'7':59,'8':60,'9':61,'+':62,'/':63,'=':0} 
    output = []
    for x in baseinput:
        x = basebindict[x]
        count  = 5
        binarylist=[]
        while count >=0:
            binarylist.append(x/2**count)
            x= x%2**count
            count-=1
        output += binarylist
    returnvalue = ''
    for x in output:
        returnvalue += str(x)
    print returnvalue
    return returnvalue
    
    
def base_to_hex(basestringinput):                                                                       
    """ converts a string of base 64 encoded text to a string of hex"""
    return bin_to_hex(base_to_bin(basestringinput))

def hex_to_base(hexinput):                                                                             
    """ converts a string of hex to a string of base64 encoded text """
    return bin_to_base(hex_to_bin(hexinput))

def dec_to_hex(decvalues, listflag = True):                                                             
    """ converts a LIST of decimal values to a LIST of hexvalues """
    # This expects the input to be a LIST if it is not and is a single value
    #False must be passed as the second argument 
    output = []
     
    hexletter = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    if listflag == True:
        for x in decvalues:
            a = x/16
            b = x%16
            if b>9:
                b = hexletter[b]
            value = "" + str(a) +str(b) +""
            output.append(value)
    elif listflag == False:
            a = decvalues/16
            b = decvalues%16
            if b>9:
                b = hexletter[b]
            value = "" + str(a) +str(b) +""
            output.append(value)
    return output #FIXME changed this output to a list. soemthing broken? (keyfreak)

def hex_to_dec(hexvalues):                                                             
    """ converts a String of hex values to a LIST of decvalues """
    # This expects the input to be a String by default if it is not and 
    # is a single hexpair True must be passed as the second argument
    output = []
    declist = []
    hexletter = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    print hexvalues
    listflag, hexvalues = inputvalidater(hexvalues,0)
    if hexvalues == "ERROR":
        print "Invalid Input ID: Core 215"
        return None
    #if listflag == False:
    output = chunks(hexvalues, 2)
    for x in output:
        if x[0] in hexletter:
            a = hexletter[x[0]]*16
        else:
            a = int(x[0])*16
        if x[1] in hexletter:
            b = hexletter[x[1]]
        else:
            b = int(x[1])
        declist.append(int(a)+int(b))     
    #elif listflag == True:
    #    if x[0] in hexletter:
    #        a = hexletter[x[0]]*16
    #    else:
    #        a = int(x[0])*16
    #    if x[1] in hexletter:
    #        b = hexletter[x[1]]
    #    else:
    #        b = int(x[1])
    #    declist.append(int(a)+int(b))
    return declist

def ascii_to_hex(ascistring):                                                                           
    """This Takes in a String of ASCII text and decodes it to a hexstring"""
    outlist = []
    for x in ascistring:
        outlist.append(ord(x))
    return ''.join(dec_to_hex(outlist))   