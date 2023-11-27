import sys
import json
import os

#I am learning about classes with python
class JSONDecodeErrorCustom(Exception):
    pass;

class JSONTokenizer:
    def __init__(self, input_str):
        self.input_str = input_str
        self.position = 0
        #print("input string : ",self.input_str)
        

    def get_next_token(self):
        #ignore space
        #print("getting next token")
        while self.position < len(self.input_str) and self.input_str[self.position].isspace():
            self.position += 1
        # End of input

        #print("input string : ",self.input_str)
        if self.position == len(self.input_str):
            return None  
        
        current_char=self.input_str[self.position]
        if current_char == '{': #OPEN OBJECT
            self.position += 1
            #print("opem")
            return ('LBRACE', '{')
        elif current_char == '}': #CLOSE OBJECT
            self.position += 1
            return ('RBRACE', '}')
        elif current_char == ':': #SEPERATES KEY : VALUE
            self.position += 1
            return ('COLON', ':')
        elif current_char == ',': #SEPARATES (key,value)
            self.position += 1
            return ('COMMA', ',')
        elif current_char == '"': #READ STRING
            return ('STRING',self.read_string())
        elif current_char.isdigit() or current_char == '-': #NUMBER
            return self.read_number()
        elif current_char.isalpha(): #KEYBOARD
            return self.read_keyword()
        else:
            raise ValueError(f"Unexpected character: {current_char}")

    def read_string(self): # Implement string reading logic
        # read till next "
        stringVal=""
        self.position+=1
        while(self.input_str[self.position]!='"'):
            stringVal+=self.input_str[self.position]
            self.position+=1
            if(self.position==len(self.input_str)): #out of bounds and still not encounted end
                #throw error
                print("error : out of bounds")
                break
        self.position+=1#current is last " so move one more
        return stringVal

    def read_number(self): # Implement number reading logic
        isNeg=False
        if(self.input_str[self.position]=='-'):
            isNeg=True
            self.position+=1
        
        #11e3 1123
        stringNum=""
        while(self.input_str[self.position].isdigit() or self.input_str[self.position]=='.'):
           
            stringNum+=self.input_str[self.position]
            self.position+=1
            if(self.position==len(self.input_str)): #out of bounds and still not encounted end
                print("error out of bounds ") #throw error
                break
        
        if(self.input_str[self.position].isalpha()):
            print("error not number")
            print(self.input_str[self.position])
        #now check if number gotten can be converted to number
        #123.231.1324 is not valid so that would be check by converting to int

        return ('NUMBER',stringNum)

    def read_keyword(self): # Implement true, false, null reading logic
        #only lower case true, false and null
        stringVal=""
        while(self.input_str[self.position].isalpha()):
            if(not(self.input_str[self.position]>='a' and self.input_str[self.position]<='z')):
                print("error in keyword")
                break
            stringVal+=self.input_str[self.position]
            self.position+=1
            if(self.position==len(self.input_str)): #out of bounds and still not encounted end
                #throw error
                break
        
        #now we are not on alpha
        print("keyword : ",stringVal)
        if(stringVal=='true'):
            return ('TRUE',True)
        elif(stringVal=='false'):
            return ('FALSE',False)
        elif(stringVal=='null'):
            return ('NULL',None)
        else:
            print("error in keyword")

        return stringVal

class JSONParser:
    def __init__(self,input_str):
        #print("input string 1 : ",input_str)
        self.lexer=JSONTokenizer(input_str)
        self.current_token=self.lexer.get_next_token()
        # print(self.current_token)
        # print(self.lexer.position)
        self.myData=None;

    def parse(self):
        print("start parsing")
        print(self.current_token)
        curr=self.getCurrentToken()
        return self.parse_value(curr)
    
    def parse_object(self): #a object {}
        print("Object START")
        temp={}

        # it should have ::  key : value :: then comma(,) or just end
        print(self.current_token) #move it ahead of { also
        while(True):
            print("current token : ",self.current_token)
            currentType,currentValue=self.current_token
            if(currentType=='RBRACE'): 
                break

            key, value =self.getKeyValuePair()

            print(key,value)
            if(key[0]=='STRING'):
                kValue=self.parse_value(key)
                vValue=self.parse_value(value)
                temp[kValue]=vValue #can check if key already present then error
                print("value pair : ",kValue,vValue)

            delim=self.getCurrentToken()
            print("delim : ",delim)
            print("current : ",self.current_token)
            delimType, delimValue=delim
            if(delimType=='RBRACE'):
                break
            if(delimType=='COMMA' and (self.current_token==None or self.current_token[0]=='RBRACE')):
                print("error : comma at end") #throw error
                break

        print("object over : ",temp)
        #now end is }
        self.getCurrentToken()#move ahead of }
        return temp
    
    def getKeyValuePair(self):
        key=self.getCurrentToken()
        
        keyType,keyValue=key
        if(keyType!='STRING'):
            print("error in type of key is not string") #throw error

        colon=self.getCurrentToken()
        colonType, colonValue=colon
        if(colonType!='COLON'):
            print("error in SYNTAX : COLON not provided") #throw error

        value=self.getCurrentToken()
        valueType,valueValue=value
        #check value type if is it correct

        print(key,colon,value)
        return (key,value)



    def getCurrentToken(self):
        current = self.current_token
        self.current_token=self.lexer.get_next_token()
        return current
    
    def parse_value(self,current_token):
        token_type, token_value = current_token #as soon as I take current token I want to move to next token : implmemnet it with function call
        #print(token_type)
        if token_type == 'LBRACE':
            return self.parse_object()
        elif token_type == 'RBRACE':
            return None  # End of input
        elif token_type == 'STRING':
            return token_value
        elif token_type == 'NUMBER':
            return float(token_value) if '.' in token_value else int(token_value)
        elif token_type == 'TRUE':
            return True
        elif token_type == 'FALSE':
            return False
        elif token_type == 'NULL':
            return None
        else:
            raise ValueError(f"Unexpected token: {token_type}")
        
    def processData(self):
        print("processing")
        self.myData={} #will add in to the value:attribute
        self.myData=self.parse()
        
    def loadData(self):
        try:
            if(self.myData==None):
                print("empty data")
                self.processData()
            return self.myData
            #raise ValueError("Simulated data loading error")
        except Exception as e:
            # Raise a custom exception with a meaningful error message
            error=f"Error loading data: {str(e)}"
            raise JSONDecodeErrorCustom(error)


def customJsonParser(file_path):
    print("\n")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path=script_dir+file_path
    try:
        with open(absolute_file_path,'r') as file:#read the file : file currently contains metadata
            #print (file.read())
            #print(type(file.read()))
            #print(file.read())#string
            stringData=file.read()
            print(stringData)
            parser= JSONParser(stringData)#JSONParser
            jsonData=parser.loadData()
            print(jsonData)
        return 0
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 2
    except JSONDecodeErrorCustom as err:
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        print(err)
        return 1
    except Exception as err:
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        print(err)
        return 1

        

#I'll implement it myself later
# I beilive the challenge did not want me to use builtin function
# but creating this flexible cli was challenge enough for today
def jsonParse(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path=script_dir+file_path
    print(absolute_file_path)
    try:
        with open(absolute_file_path,'r') as file:
            #read the file : file currently contains metadata
            #print (file.read())
            #print(type(file.read()))
            #print(file)
            json_data=json.load(file)
            #print(json_data)
        print("JSON file loaded successfully:")
        print(json.dumps(json_data, indent=2))  # Display JSON content with indentation and style
        return 0
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 2
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        return 1


def ccjson(parser,arguments):
    if(arguments[0]=='-h') :
        parser.print_help()
        return
    

    args=parser.parse_args(arguments)

    if not sys.stdin.isatty() or not args.files:
        #nothing file provided
        a=1
    elif args.files:
        for file_path in args.files:
            valid=jsonParse(file_path)
            #valid=customJsonParser(file_path)
            print(valid)
    else:# If no files or stdin, print help
        print("Weird Command : use ccwc -h or ccwc --help to access help")
        parser.print_help()
    return

#automating test
files=['\\tests\\step1\\invalid.json','\\tests\\step1\\valid.json','\\tests\\step2\\invalid.json','\\tests\\step2\\invalid2.json','\\tests\\step2\\valid.json','\\tests\\step2\\valid2.json','\\tests\\step3\\invalid.json','\\tests\\step3\\valid.json','\\tests\\step4\\invalid.json','\\tests\\step4\\valid.json','\\tests\\step4\\valid2.json']
for file in files:
    #print(file)
    val=customJsonParser(file)
    #print(val)