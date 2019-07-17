
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def get_data(self):
        return self.data

expression = ""
expressionArray = []

operators = {
    "NOT": 2, "¬": 2, "~": 2, "!": 2,

    "AND": 1, "∧": 1, "^": 1, "/\\": 1, "&&": 1,

    "OR": 0, "∨": 0, "\\/": 0, "||": 0,

    "->": -1, "=>": -1, "→": -1
}

finalOperatorSymbols = {
    2: "¬",
    1: "∧",
    0: "∨",
    -1: "→"
}
vars = []
expIndex = 0 
varDict = {} 
postfixExpression =[]
expressionTree = Node(None)


def is_valid():
    
    parenthesesBalance = 0
    operatorBalance = 0
    previousElement = ""
    if len(expressionArray) < 3:
        print("INVALID EXPRESSION - less than 3 elements")
        return False
    
    for element in expressionArray:
        
        if element == "(":
            parenthesesBalance += 1
        elif element == ")":
            parenthesesBalance -= 1
            if parenthesesBalance < 0 :
                print("INVALID EXPRESSION - Too many close parentheses")
                return False
        elif element in operators and operators[element] != 2:

            if previousElement in operators and operators[previousElement] == 2:
                print('INVALID EXPRESSION - Invalid operator/variable order: "' + previousElement, element + '"')
                return False
            else:
                operatorBalance -= 1
                
        elif not element in operators: # if element is a variable
            operatorBalance += 1
        
        if operatorBalance < 0 or operatorBalance > 1:
            print('INVALID EXPRESSION - Invalid operator/variable order: "' + previousElement + " " + element, '"')
            return False 
        previousElement = element
    if parenthesesBalance > 0 :
        print("INVALID EXPRESSION - Too many open parentheses")
        return False
    return True


def build_postfix_expression():
    operatorStack = []
    for element in expressionArray:
        if element in operators:
            # if len(operatorStack) > 0 and operatorStack[-1] != "(" and operators[element] < operators[operatorStack[-1]]:
            while len(operatorStack) > 0 and operatorStack[-1] != "(" and operators[operatorStack[-1]] > operators[element]:
                postfixExpression.append(operatorStack.pop())
            operatorStack.append(element)
        elif element == "(":
            operatorStack.append(element)
        elif element == ")":
            while operatorStack[-1] != "(":
                postfixExpression.append(operatorStack.pop())
            operatorStack.pop()
        else:
            postfixExpression.append(element)
            if not element in vars:
                vars.append(element)
    while len(operatorStack) > 0:
        postfixExpression.append(operatorStack.pop())

def build_expression_tree():
    nodeStack = []
    global expressionTree
    for element in postfixExpression:
        if element in operators:
            newNode = Node(element)
            newNode.left = nodeStack.pop()
            if operators[element] != 2:
                newNode.right = nodeStack.pop()
            nodeStack.append(newNode)
        else:
            nodeStack.append(Node(element))
    expressionTree = nodeStack.pop()

def expression_value(currentNode):
    if not currentNode.data in operators:
        return varDict[currentNode.data]
    elif operators[currentNode.data] == -1: # Implication
        return not (not expression_value(currentNode.left) and expression_value(currentNode.right))
    elif operators[currentNode.data] == 0: # OR
        return expression_value(currentNode.left) or expression_value(currentNode.right)
    elif operators[currentNode.data] == 1: # AND
        return expression_value(currentNode.left) and expression_value(currentNode.right)
    elif operators[currentNode.data] == 2: # NOT
        return not expression_value(currentNode.left)

def print_line_number(i):
    global expIndex
    global varDict
    for v in range(len(vars)):
        tempBool = (i // ((2**len(vars)) // (2**(v+1)) )) % 2 == 1  
        varDict[vars[v]] = tempBool
        print(varDict[vars[v]], end=' ')
        if tempBool: print(end=' ') # Prints space after "True"
        if len(vars[v]) > 5:
            for q in range(len(vars[v]) - 5):
                print(end=' ')

    print("|", expression_value(expressionTree))


def create_truth_table():
    headerLineLen = 0
    for v in vars:
        print(v, end=' ')
        headerLineLen += len(v) + 1
        if len(v) < 5:
            for i in range(abs(5 - len(v))):
                print(end=' ')
                headerLineLen += 1
        
    print("|", expression)
    for i in range(headerLineLen + len(expression) + 1):
        print('=', end='')
    print()
    for i in range(2**len(vars)):
        print_line_number(i)


print('''

Welcome to Victor's Truth Table Generator!
========================================================
Operators:   [ "NOT", "AND", "OR" ] (in order of precedence)
Parentheses: [ "(", ")" ]
Anything else is considered a variable
Everything is case insensitive

''')

while True:
    expression = input("> ")
    if expression.lower() == "quit": break

    for key in operators.keys():
        # print(key)
        if key != "NOT" and key != "AND" and key != "OR":
            expression = expression.replace(key, " " + key + " ")
    
    expressionArray = expression.replace("(", " ( ").replace(")", " ) ").split()
    # print(expressionArray)
    expression = ""

    for i in range(len(expressionArray)):
        if expressionArray[i].upper() in operators:
            expressionArray[i] = finalOperatorSymbols[operators[expressionArray[i].upper()]]
        if(expressionArray[i] == finalOperatorSymbols[operators["NOT"]] or expressionArray[i] == "(" or (i < len(expressionArray) - 1 and expressionArray[i+1] == ")")):
            expression += expressionArray[i]
        else:
            expression += expressionArray[i] + " "
        # if expressionArray[i] == "(" or (i < len(expressionArray) - 1 and expressionArray[i+1] == ")"):
        #     expression += expressionArray[i]
        # else:
        #     expression += expressionArray[i] + " "

    vars = []
    postfixExpression = []

    print("\n\n")
    if is_valid():
        build_postfix_expression()
        build_expression_tree()
        create_truth_table() 
    print("\n\n")   

