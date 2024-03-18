def add(line: str ,val1:int, val2:int):

    """Does the addition between val1 and val2 refers to the function ADD in RAM machines
    -----------
    Parameters:
        line(str): code line read in the file.txt used in the project
        val1 (int): int part of the addition 
        val2 (int): int part of the addition
    """
    

    res = val1 + val2 

def sub(line: str, val1: int, val2: int):

    """Does the substraction between val1 and val2 refers to the function SUB in RAM machines
    -----------
    Parameters:
        line(str): code line read in the file.txt used in the project
        val1 (int): int part of the substraction
        val2 (int): int part of the substraction 
    """

    res = val1 - val2

def div(line:str , val1:int, val2:int):
    """
    Does the division of val1 by val2 and rounds the result at two values after the coma, refers to the function Div in RAM machines
    -----------
    Parameters:
        line(str): code line read in the file.txt used in the project
        val1(int): int that is divided by val2
        val2(int): int that divides val1
    """
    res = round(val1 / val2, 2)
