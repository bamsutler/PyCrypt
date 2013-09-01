import grouper
import b64_mod

##################################################################################        
def hextobin (number):
    """function to convert hex to bin input is a hexstring output is a bin string"""
    #hex to binary code here
    target = []
    for x in number:
        target.append(x)
    newlist = []
    for x in target:
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
       newlist.append(hex_bindict[x])
    binstring = '' 
    binstring = ''.join(newlist)
    return binstring        
################################################################################       
def bintobase (number):
    """ Function to convert binary strings to a Base64 encription"""
    #binary to base64 code here
    binstring = number
    finalsixstring = ''       
    basedict= {0:'A',1:'B',2:'C',3:'D',4:'E',
            5:'F',6:'G',7:'H' ,8:'I' ,9:'J' ,10:'K' ,
            11:'L' ,12:'M' ,13:'N' ,14:'O' ,15:'P' ,16:'Q' ,17:'R' ,18:'S' ,19:'T' ,20:'U',
            21:'V' ,22:'W' ,23:'X' ,24:'Y' ,25:'Z' ,26: 'a',27:'b' ,28:'c' ,29:'d' ,30:'e',
            31:'f' ,32:'g' ,33:'h' ,34:'i' ,35:'j' ,36:'k' ,37:'l' ,38:'m' ,39:'n' ,40:'o',
            41:'p' ,42:'q' ,43:'r' ,44:'s' ,45:'t' ,46:'u' ,47:'v' ,48:'w' ,49:'x' ,50:'y',
            51:'z' ,52:'0' ,53:'1' ,54:'2' ,55:'3' ,56:'4' ,57:'5' ,58:'6' ,59:'7' ,60:'8',
            61:'9' ,62:'+' ,63:'/'}
        
        
        
    tup = grouper.grouper(binstring, 6, 0)
    sixchar = ''
    outlist = []
    for x in tup:
        sixchar = ''.join(x)
        #print sixchar
        total =0
        count =5
        for y in sixchar:
            total += int(y)*2**count
            count -= 1
        #print total    
        # Totals are correct here indexes are found now to implemenet the Base64 dict.    
        outlist.append(basedict[total])
    finalsixstring = ''.join(outlist)
    return finalsixstring        
        
        
 ################################################################################       
def basetobin(number):
    """ This function converts a Base64 encoded string to binary"""
    target = number
    valueList = []
    fulllist = []
    outputstring= ''
    #Base64 to binary code here
    rbasedict = { 'A':0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
            'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
            'V':21,'W':22,'X':23,'Y':24,'Z':25,'a':26,'b':27,'c':28,'d':29,'e':30,
            'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,
            'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,
            'z':51,'0':52,'1':53,'2':54,'3':55,'4':56,'5':57,'6':58,'7':59,'8':60,'9':61,'+':62,'/':63}
    for x in target:
        valueList.append(rbasedict[x])
    #print valueList
    for x in valueList:
        c=5
        binarylist=[]
        while c>=0:
            binarylist.append(x/2**c)
            x= x%2**c
            c-=1
        fulllist=fulllist+binarylist
    for x in fulllist:
        outputstring+= str(x)
    return outputstring   
   
   
##################################################################################    
def bintohex(binlist):
    """ converts binary strings to hex strings"""
    hexstring=''
        #binary to hex code here
    rhex_bindict= {'0000':'0',
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
    madestring = ''
    for x in binlist:
        madestring = madestring + str(x)
    tup =grouper.grouper(madestring, 4, None)     
    fourchar = ''
    binlist = []
    for x in tup:
        fourchar = ''.join(x)     
        binlist.append(fourchar)
    madelist = []
    for x in binlist:
        madelist.append(rhex_bindict[x])
    hexstring = ''.join(madelist)
    return hexstring    
#################################################################################
def hextobase(hexstring):
    """Converts a Hex string to a BASE64 String"""
    binstring = b64_mod.hextobin(hexstring)
    b64string = b64_mod.bintobase(binstring)
    return b64string
#############################################################################  
def basetohex(b64string):
    """ converts a BASE64 string to a HEX string """
    binstring = b64_mod.basetobin(b64string)
    hexstring = b64_mod.bintohex(binstring)
    return hexstring     
       
#############################################################################
def dec_to_hex(decvalues, listflag = True):
    """ converts a LIST of decimal values to a LIST of hexvalues """
    # This expects the input to be a LIST if it is not and is a single value
    #False must be passed as the second argument ### output is still a list ###
    output = []
     
    hexletter = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    if listflag == True:
        if inputvalidater(decvalues) == False: 
            return "BROKE NUCKKA " + str(decvalues)
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
#############################################################    
def hextodec(hexvalues,flag = 0):
    """ recives a string of hex values to be converted into correct decimal notation to be chr() into letters """
    output = []
    declist = []
    hexletter = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    print inputvalidater(hexvalues)
    if flag == 0:
        output = grouper.chunks(hexvalues, 2)
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
    elif flag == 1:
        if x[0] in hexletter:
            a = hexletter[x[0]]*16
        else:
            a = int(x[0])*16
        if x[1] in hexletter:
            b = hexletter[x[1]]
        else:
            b = int(x[1])
        declist.append(int(a)+int(b))
        print declist  
    return declist
#############################################################################
def ascitohex(ascistring):
    outlist = []
    for x in ascistring:
        outlist.append(ord(x))
    return ''.join(b64_mod.dec_to_hex(outlist))    
    
def inputvalidater(inputstring):
    """takes the given input string an checks it to make sure 
    there are an even number of charicters"""
    returnvalue = False
    if type(inputstring) is str:
        if len(inputstring)%2 ==0:
            return True
    elif type(inputstring) is list:
        size = len(inputstring[0])
        
        for x in inputstring:
            if len(x) == size:
                returnvalue = True
    return returnvalue
                            
