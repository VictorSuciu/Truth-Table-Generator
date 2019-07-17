# Truth Table Generator

This console program generates truth tables from boolean expressions.

-----

## Installation

1. Download the file `Truth_Table_Generator.py`.
2. Navigate into its parent directory in the command line. 
3. Enter the following command: `python3 Truth_Table_Generator.py`.
4. Done! You can now enter boolean expressions and generate truth tables.

-----

## Expression Syntax 

### Operators, in order of precedence:
* Negation: `NOT, ~, ¬`
* Conjunction: `AND, /\, ^, ∧`
* Disjunction: `OR, \/, ∨`
> Not case sensitive

### Parentheses:
* (
* )

### Variables
Any other string is considered a variable

#### Variables and Operators must be separated by a blank space. This is optional for parentheses.

-----

## Sample Inputs and Outputs

Input Expression

```
Cat OR NOT Dog
```

Output Truth Table

```
Cat   Dog   | Cat ∨ ¬Dog 
========================
False False | True
False True  | False
True  False | True
True  True  | True
```

<br>

Input Expression
```
(w OR x) AND (y OR z)
```

Output Truth Table
```
w     x     y     z     | (w ∨ x) ∧ (y ∨ z) 
===========================================
False False False False | False
False False False True  | False
False False True  False | False
False False True  True  | False
False True  False False | False
False True  False True  | True
False True  True  False | True
False True  True  True  | True
True  False False False | False
True  False False True  | True
True  False True  False | True
True  False True  True  | True
True  True  False False | False
True  True  False True  | True
True  True  True  False | True
True  True  True  True  | True
```
