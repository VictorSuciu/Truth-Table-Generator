# Truth Table Generator

This console program generates truth tables from boolean expressions.

-----

## Installation

1. Install [Python 3.x](https://www.python.org/downloads/)
2. Download the file `Truth_Table_Generator.py`.
3. Navigate into its parent directory in the command line. 
4. Enter the following command: `python3 Truth_Table_Generator.py`
5. Done! You can now enter boolean expressions and generate truth tables.

-----

## Expression Syntax 

### Operators, in order of highest to lowest precedence:
| Operator Type | Supported Notations |
|:-------------:|:-------------------:|
|    Negation   |`NOT` `~` `¬` `!`|
|  Conjunction  |`AND` `/\` `^` `∧` `&&`|
|  Disjunction  |`OR` `\/` `∨` `\|\|`|
|   Inference   |`->` `=>`  `→`|
> NOTE: Not case sensitive. Word operators (NOT, AND, OR) must be separated by a blank space. This is not required for any other operator notations.
### Parentheses:
* (
* )

### Variables
Any other string is considered a variable

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

<br>

Input Expression
```
(p || q) -> (p && !(r -> q))
```

Output Truth Table
```
p     q     r     | (p ∨ q) → (p ∧ ¬(r → q)) 
============================================
False False False | True
False False True  | True
False True  False | False
False True  True  | False
True  False False | False
True  False True  | True
True  True  False | False
True  True  True  | False
```
