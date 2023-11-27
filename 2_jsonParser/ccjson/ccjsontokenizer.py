# todo : REPlace the magic values with enums

class JSONTokenizer:
    def __init__(self, input_str):
        self.input_str = input_str
        self.position = 0

    def get_next_token(self):
        while self.position < len(self.input_str) and self.input_str[self.position].isspace():
            self.position += 1 #ignore space
        
        if self.position == len(self.input_str):
            return None  # End of input
        
        current_char=self.input_str[self.position]
        if current_char == '{': #OPEN OBJECT
            self.position += 1
            return ('LBRACE', '{')
        elif current_char == '}': #CLOSE OBJECT
            self.position += 1
            return ('RBRACE', '}')
        elif current_char == '[': #OPEN ARRAY
            self.position+=1
            return ('LBRACKET','[')
        elif current_char==']': #CLOSE ARRAY
            self.position+=1
            return ('RBRACKET',']')
        elif current_char == ':': #SEPERATES KEY : VALUE (key and value)
            self.position += 1
            return ('COLON', ':')
        elif current_char == ',': #SEPARATES (key,value)
            self.position += 1
            return ('COMMA', ',')
        elif current_char == '"': #READ STRING
            return ('STRING',self.read_string())
        elif current_char.isdigit() or current_char == '-': #NUMBER
            return self.read_number()
        elif current_char.isalpha(): #KEYWORD
            return self.read_keyword()
        else:
            raise ValueError(f"Unexpected character: {current_char}")

    def read_string(self): # Implement string reading logic
        if self.input_str[self.position] != '"':
            raise ValueError("String must start with '\"'")
        
        stringVal="" # read till next "
        self.position+=1
        while(self.input_str[self.position]!='"'):
            stringVal+=self.input_str[self.position]
            self.position+=1
            if(self.position==len(self.input_str)): #out of bounds and still not encounted end
                raise IndexError("ERROR : out of bounds")
                break
        self.position+=1 #current is last " so move one more
        return stringVal

    def read_number(self): # Implement number reading logic
        #11e3 1123
        stringNum=""

        isNeg=False
        if(self.input_str[self.position]=='-'):
            isNeg=True
            self.position+=1
            stringNum+='-'
        
        while(self.input_str[self.position].isdigit() or self.input_str[self.position]=='.'):
            stringNum+=self.input_str[self.position]
            self.position+=1
            if(self.position==len(self.input_str)): #out of bounds and still not encounted end
                raise IndexError("ERROR : out of bounds")
                break
        
        if(self.input_str[self.position].isalpha()):
            raise ValueError(f"ERROR : not a number : ${self.input_str[self.position]}")

        #now check if number gotten can be converted to number
        #123.231.1324 is not valid so that would be check by converting to int : when parse value
        return ('NUMBER',stringNum)

    def read_keyword(self): # Implement true, false, null reading logic
        stringVal="" #only lower case true, false and null
        while(self.input_str[self.position].isalpha() or self.input_str[self.position].isdigit()):
            stringVal+=self.input_str[self.position]
            self.position+=1
            if(self.position==len(self.input_str)): #out of bounds and still not encounted end
                raise IndexError("ERROR : out of bounds")
        
        #now we are not on alpha : KEYWORD
        if(stringVal=='true'):
            return ('TRUE',True)
        elif(stringVal=='false'):
            return ('FALSE',False)
        elif(stringVal=='null'):
            return ('NULL',None)
        else:
            raise Exception(f"ERROR : keyword {stringVal} not accepted") #throw error

        return stringVal