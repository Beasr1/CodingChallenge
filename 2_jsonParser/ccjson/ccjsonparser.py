from ccjson.ccjsontokenizer import JSONTokenizer
from ccjson.ccjsonCustomException import JSONDecodeErrorCustom


class JSONParser:
    def __init__(self,input_str):
        self.lexer=JSONTokenizer(input_str)
        self.current_token=self.lexer.get_next_token()
        self.myData=None;

    def parse(self):
        curr=self.getCurrentToken()
        return self.parse_value(curr)
    
    def parse_object(self): #a object {}
        temp={}

        # it should have ::  key : value :: then comma(,) or just end
        while(True):
            currentType,currentValue=self.current_token
            if(currentType=='RBRACE'): 
                break

            key, value =self.getKeyValuePair()

            temp[key]=value #can check if key already present then error
            print("key : value ==> ",key,value)

            delim=self.current_token
            delimType, delimValue=delim
            if(delimType=='RBRACE'):
                break

            self.getCurrentToken()
            if(delimType=='COMMA' and (self.current_token==None or self.current_token[0]=='RBRACE')):
                raise Exception("ERROR : Trailing Comma")
            
        self.getCurrentToken()# now end is } : move ahead of }
        return temp
    
    def parse_array(self):
        temp=[]

        # it should have ::  element :: then comma(,) or just end
        while(True):
            currentType,currentValue=self.current_token
            if(currentType=='RBRACKET'): 
                break

            element=self.parse_value(self.current_token)

            #print(element)
            temp.append(element)

            delim=self.current_token
            delimType, delimValue=delim
            if(delimType=='RBRACKET'):
                break
            self.getCurrentToken()#move ahead
            if(delimType=='COMMA' and (self.current_token==None or self.current_token[0]=='RBRACKET')):
                raise Exception("ERROR : Trailing Comma")
        self.getCurrentToken()#move ahead of ]
        return temp
    
    def getKeyValuePair(self):
        key=self.getCurrentToken()
        keyType,keyValue=key
        if(keyType!='STRING'):
            raise Exception("TYPE ERROR : key is not string")

        colon=self.getCurrentToken()
        colonType, colonValue=colon
        if(colonType!='COLON'):
            raise Exception("SYNTAX ERROR : COLON not provided")

        value=self.getCurrentToken()
        valueType,valueValue=value
        #check value type if is it correct

        #print(key,colon,value)
        keyValue=self.parse_value(key)
        valueValue=self.parse_value(value) #will give the value
        return (keyValue,valueValue)

    def getCurrentToken(self):
        current = self.current_token
        self.current_token=self.lexer.get_next_token()
        return current
    
    def parse_value(self,current_token):
        token_type, token_value = current_token #as soon as I take current token I want to move to next token : implmemnet it with function call
        if token_type == 'LBRACE':
            return self.parse_object() #start parsing object
        elif token_type=='LBRACKET':
            return self.parse_array() #start parsing array
        elif token_type == 'RBRACE':
            return None # End of object
        elif token_type=='RBRACKET':
            return None # end of array
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
        self.myData=self.parse()
        
    def loadData(self):
        try:
            if(self.myData==None):
                self.processData()
            return self.myData
        except Exception as e:
            # Raise a custom exception with a meaningful error message
            error=f"Error loading data: {str(e)}"
            raise JSONDecodeErrorCustom(error)