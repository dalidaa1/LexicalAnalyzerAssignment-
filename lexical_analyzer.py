
# Converted by Dalia Mahmoud - 200046463

# Token types
LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOF = -1

# Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

class LexicalAnalyzer:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.charClass = None
        self.currentChar = ''
        self.lexeme = ''
        self.getChar()

    def addChar(self):
        self.lexeme += self.currentChar

    def getChar(self):
        if self.index < len(self.text):
            self.currentChar = self.text[self.index]
            self.index += 1
            if self.currentChar.isalpha():
                self.charClass = LETTER
            elif self.currentChar.isdigit():
                self.charClass = DIGIT
            else:
                self.charClass = UNKNOWN
        else:
            self.charClass = EOF

    def getNonBlank(self):
        while self.currentChar.isspace():
            self.getChar()

    def lookup(self, ch):
        if ch == '(':
            self.addChar()
            return LEFT_PAREN
        elif ch == ')':
            self.addChar()
            return RIGHT_PAREN
        elif ch == '+':
            self.addChar()
            return ADD_OP
        elif ch == '-':
            self.addChar()
            return SUB_OP
        elif ch == '*':
            self.addChar()
            return MULT_OP
        elif ch == '/':
            self.addChar()
            return DIV_OP
        else:
            self.addChar()
            return EOF

    def lex(self):
        self.lexeme = ''
        self.getNonBlank()

        if self.charClass == LETTER:
            self.addChar()
            self.getChar()
            while self.charClass in [LETTER, DIGIT]:
                self.addChar()
                self.getChar()
            token = IDENT

        elif self.charClass == DIGIT:
            self.addChar()
            self.getChar()
            while self.charClass == DIGIT:
                self.addChar()
                self.getChar()
            token = INT_LIT

        elif self.charClass == UNKNOWN:
            token = self.lookup(self.currentChar)
            self.getChar()

        elif self.charClass == EOF:
            self.lexeme = 'EOF'
            token = EOF

        print(f"Next token is: {token}, Next lexeme is: {self.lexeme}")
        return token


input_expr = "(sum + 47) / total"
analyzer = LexicalAnalyzer(input_expr)

while True:
    token = analyzer.lex()
    if token == EOF:
        break
