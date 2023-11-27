from ccjsontokenizer import JSONTokenizer

class JSONParser:
    def __init__(self,input_str):
        self.lexer=JSONTokenizer(input_str)
        self.current_token=self.lexer.get_next_token()
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

            delim=self.current_token
            print("delim and current : ",delim)
            delimType, delimValue=delim
            if(delimType=='RBRACE'):
                break
            if(delimType=='COMMA' and (self.current_token==None or self.current_token[0]=='RBRACE')):
                print("error : comma at end") #throw error
                break
            self.getCurrentToken()

        print("object over : ",temp)
        #now end is }
        self.getCurrentToken()#move ahead of }
        return temp
    
    def parse_array(self):
        print("ARRAY START")
        temp=[]
        # it should have ::  key : value :: then comma(,) or just end
        print(self.current_token) #move it ahead of { also
        while(True):
            print("current token : ",self.current_token)
            currentType,currentValue=self.current_token
            if(currentType=='RBRACKET'): 
                break

            element=self.parse_value(self.current_token)

            print(element)
            temp.append(element)


            delim=self.current_token
            print("delim and current : ",delim)
            delimType, delimValue=delim
            if(delimType=='RBRACKET'):
                break
            if(delimType=='COMMA' and (self.current_token==None or self.current_token[0]=='RBRACKET')):
                print("error : comma at end") #throw error
                break

            self.getCurrentToken()#move ahead

        self.getCurrentToken()#move ahead of ]
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
        elif token_type=='LBRACKET':
            return self.parse_array()
        elif token_type == 'RBRACE':
            return None  # End of input
        elif token_type=='RBRACKET':
            return None
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