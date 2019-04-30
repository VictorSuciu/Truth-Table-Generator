
expression = "g OR (h AND j)"
expressionArray = expression.replace("(", " ( ").replace(")", " ) ").split()

operators = {
    "AND": 2,
    "OR": 2,
    "NOT": 2,
    "(": 1,
    ")": -1
}

vars = []

def count_vars_check_validity():
    
    parenthesesBalance = 0
    operatorBalance = 2

    if len(expressionArray) < 3:
        print("INVALID EXPRESSION - less than 3 elements")
        return
    
    for index in range(len(expressionArray)):

        currentElement = operators.get(expressionArray[index], -2)

        if abs(currentElement) == 2:
            operatorBalance += currentElement
            if operatorBalance != 0 and operatorBalance != 2:
                print("INVALID EXPRESSION - Invalid operator/variable order ", operatorBalance)
                return
            if currentElement == -2:
                vars.append(expressionArray[index])

        elif abs(currentElement) == 1:
            parenthesesBalance += currentElement
            if parenthesesBalance < 0 :
                print("INVALID EXPRESSION - Too many close parentheses")
                return
        
    if parenthesesBalance != 0 or operatorBalance != 0:
        print("INVALID EXPRESSION - Too many open parentheses or one-too-many operators | ", 
              parenthesesBalance, " ", operatorBalance)
        return

varDict = {} 
expIndex = 0 
def print_line_number(i):
    global expIndex
    for v in range(len(vars)):
        # print("VALUE: ", len(vars))
        tempBool = bool(  (i // ((2**len(vars)) // (2**(v+1)) )) % 2 == 0  )
        varDict[vars[v]] = tempBool
        print(tempBool, end=' ')
        if tempBool: print(end=' ')
    expIndex = len(expressionArray)
    print(expression_value(True))


 
def expression_value(value):
    global expIndex
    expIndex -= 1
    if(expIndex < 0):
        return value
    elif(expressionArray[expIndex] == "AND"):
        return value and expression_value(value)
    elif(expressionArray[expIndex] == "OR"):
        return value or expression_value(value)
    elif(expressionArray[expIndex] == "NOT"):
        return not expression_value(value)
    elif(expressionArray[expIndex] == "("):
        return value
    elif(expressionArray[expIndex] == ")"):
        return expression_value(expression_value(value))
    else:
        return expression_value(varDict.get(expressionArray[expIndex]))
        

def create_truth_table():
    for v in vars:
        print(v, "    ", end='')
    print(expression)
    for i in range(((len(vars)) * 6) + len(expression)):
        print('=', end='')
    print()
    for i in range(2**len(vars)):
        print_line_number(i)

print("\n\n\n")
count_vars_check_validity()
create_truth_table() 
print("\n\n\n")   

