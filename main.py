from typing import Union
import argparse

# question 1
def read_RAM(file_name: any, word: Union[list, int]) -> dict:

    """
    Cette fonction permet de lire un fichier texte contenant le code
    d'une machine RAM et d'initialiser la structure de données pour représenter cette machine.

    """

    lenth_word = len(word)
    program = {}
    lin = {}
    inp = {0: lenth_word}
    reg = {}
    out = {0: 0}
    stp = 0

    with open(file_name, 'r') as file:
        lines = file.readlines()
        lenth_read = len(lines)
        for idx in range(lenth_read):
            elements = lines[idx].strip().split()
            operation = elements[0][:-2] # operation gets the line without '\n'
            lin.update({idx: operation})

    for idx in range(1, lenth_word + 1):
        inp.update({idx: word[idx-1]})

    program["l"] = lin; program["i"] = inp; program["r"] = reg; program["o"] = out; program["s"] = stp
    
    # Affichage formaté de la clé "l"
    print("Initialization of RAM \n")
    for key, value in lin.items():
        if key == program["s"]:
            print(f"{value}")
        else:
            print(f"{value}")
    print("\n")
    print("code initialized successfully\n\n")
    print(f"machine initialization: \n\n{program}")

    return program

def tree_construction(program:dict)-> list:
    nil_list = [0 for i in range(len(program['l']))]
    tree =[nil_list for i in range(len(program['l']))]
    

# question 2 / 3 / 4
def execution(machine: dict):

    """
    Executes the commands of the RAM machine.

    Args:
    machine (dict): The dictionary representing the RAM machine.

    Returns:
    str: Execution status message.
    """

    line_nb = machine ['s']
    cmd_line = machine['l'][line_nb]
    
    print("RAM execution status:\n")
    for key, value in machine['l'].items():
        if key == machine["s"]:
            print(f"{value} <-- program is executing this step at the moment")
        else:
            print(f"{value}")
    print("\n")
    val_pos = ['i', 'r', 'o']
    idx_at = []
    idx_vir = []
    idx_par = []
    cmd = ''
    for idx in range(3):
        cmd += cmd_line[idx]

    ###                                         HANDLING OF ADD (addition)
   
    if cmd == 'ADD':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)

        op_2 = cmd_line[idx_vir[0]+1:idx_vir[1]] ### op 1 trough 3 are each args of the cmd line the code gets them through slicing
        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]] ### op1 is what is between '(' and ',' op2 is whats between ',' and ','
        op_3 = cmd_line[idx_vir[1]+1:idx_par[1]] ### and op3 is what's between ',' and ')'

        if '@' in op_1: # parsing of each args checking if there is a @ if so we take what's befor as the target register and what's after for the index key
            reg = op_1[:1]
            loc = op_1[2:]
            val = machine[loc[0]][int(loc[1])]
            op_1 = machine[reg][val]
        elif '-' in op_1:# check if tne value is negative it is separated from the isdigit test because using isdigit on -4 returns false  
            op_1 = int(op_1)
        elif op_1.isdigit():
            op_1 = int(op_1) 
        elif op_1[0] in val_pos: #checks if the element at index 0 in op1 is one of the letters of ['i', 'r', 'o'] 
            op_1 = machine[op_1[0]][int(op_1[1])]
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif '-' in op_2:
            op_2 = int(op_2)
        elif op_2.isdigit():
            op_2 = int(op_2) 
        elif op_2[0] in val_pos:
            op_2 = machine[op_2[0]][int(op_2[1:])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 + op_2
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1:])] = op_1 + op_2
            machine['s'] += 1

    ###                                         HANDLING OF SUB (substraction)
    elif cmd == 'SUB':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)
        
        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]] 
        op_2 = cmd_line[idx_vir[0]+1:idx_vir[1]]
        op_3 = cmd_line[idx_vir[1]+1:idx_par[1]]

        if '@' in op_1:
            reg = op_1[:1]
            loc = op_1[2:]
            val = machine[loc[0]][int(loc[1])]
            op_1 = machine[reg][val]
        elif '-' in op_1:
            op_1 = int(op_1)
        elif op_1.isdigit():
            op_1 = int(op_1) 
        elif op_1[0] in val_pos:
            op_1 = machine[op_1[0]][int(op_1[1])]
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif '-' in op_2:
            op_2 = int(op_2)
        elif op_2.isdigit():
            op_2 = int(op_2) 
        elif op_2[0] in val_pos:
            op_2 = machine[op_2[0]][int(op_2[1:])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 - op_2
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = op_1 - op_2
            machine['s'] += 1

    ###                                         HANDLING OF MLT (multiply)

    elif cmd == 'MLT':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)

        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]] 
        op_2 = cmd_line[idx_vir[0]+1:idx_vir[1]]
        op_3 = cmd_line[idx_vir[1]+1:idx_par[1]]

        if '@' in op_1:
            reg = op_1[:1]
            loc = op_1[2:]
            val = machine[loc[0]][int(loc[1])]
            op_1 = machine[reg][val]
        elif '-' in op_1:
            op_1 = int(op_1)
        elif op_1.isdigit():
            op_1 = int(op_1) 
        elif op_1[0] in val_pos:
            op_1 = machine[op_1[0]][int(op_1[1])]
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif '-' in op_2:
            op_2 = int(op_2)
        elif op_2.isdigit():
            op_2 = int(op_2) 
        elif op_2[0] in val_pos:
            op_2 = machine[op_2[0]][int(op_2[1:])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 * op_2
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = op_1 * op_2
            machine['s'] += 1

    ###                                         HANDLING OF DIV (division)
    elif cmd == 'DIV':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)

        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]]
        op_2 = cmd_line[idx_vir[0]+1:idx_vir[1]]
        op_3 = cmd_line[idx_vir[1]+1:idx_par[1]]

        if '@' in op_1:
            reg = op_1[:1]
            loc = op_1[2:]
            val = machine[loc[0]][int(loc[1])]
            op_1 = machine[reg][val]
        elif '-' in op_1:
            op_1 = int(op_1)
        elif op_1.isdigit():
            op_1 = int(op_1) 
        elif op_1[0] in val_pos:
            op_1 = machine[op_1[0]][int(op_1[1])]
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif '-' in op_2:
            op_2 = int(op_2)
        elif op_2.isdigit():
            op_2 = int(op_2) 
        elif op_2[0] in val_pos:
            op_2 = machine[op_2[0]][int(op_2[1:])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = round(op_1 / op_2, 2)
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = round(op_1 / op_2, 2)
            machine['s'] += 1

    ###                                         HANDLING OF JMP (Jump at arg)

    elif cmd == 'JMP':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
        op = cmd_line[idx_par[0]+1:idx_par[1]]
        if '-' in op:
            machine['s'] += int(op)
            print(f"Status of the machine: \n\n{machine}\n\n")
            return execution(machine)
        else:
            machine['s'] += int(op)
            print(f"Status of the machine: \n\n{machine}\n\n")
            return execution(machine)

    ###                                         HANDLING OF JEQ (Jump at op_3 if op_1 is equal to op_2 )

    elif cmd == 'JEQ':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)

        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]] 
        op_2 = cmd_line[idx_vir[0]+1:idx_vir[1]]
        op_3 = cmd_line[idx_vir[1]+1:idx_par[1]]

        if '@' in op_1:
            reg = op_1[:1]
            loc = op_1[2:]
            val = machine[loc[0]][int(loc[1])]
            op_1 = machine[reg][val]
        elif '-' in op_1:
            op_1 = int(op_1)
        elif op_1.isdigit():
            op_1 = int(op_1) 
        elif op_1[0] in val_pos:
            op_1 = machine[op_1[0]][int(op_1[1])]
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif '-' in op_2:
            op_2 = int(op_2)
        elif op_2.isdigit():
            op_2 = int(op_2) 
        elif op_2[0] in val_pos:
            op_2 = machine[op_2[0]][int(op_2[1:])]

        if op_1 == op_2:
            for i in op_3:
                if i == '-':
                    min = op_3.index('-')
                    val = int(op_3)
                    machine['s'] = machine['s'] + val
                    print(f"Status of the machine: \n\n{machine}\n\n")
                    return execution(machine)
                elif '-' not in op_3:
                    machine['s'] += int(op_3)
                    print(f"Status of the machine: \n\n{machine}\n\n")
                    return execution(machine)  
        else:
            machine['s'] += 1
            print(f"Status of the machine: \n\n{machine}\n\n")
            return execution(machine)

    ###                                         HANDLING OF JLA (Jump to op_3 if op_1 is strictly greater than op_2)

    elif cmd == 'JLA':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)

        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]] 
        op_2 = cmd_line[idx_vir[0]+1:idx_vir[1]]
        op_3 = cmd_line[idx_vir[1]+1:idx_par[1]]

        if '@' in op_1:
            reg = op_1[:1]
            loc = op_1[2:]
            val = machine[loc[0]][int(loc[1])]
            op_1 = machine[reg][val]
        elif '-' in op_1:
            op_1 = int(op_1)
        elif op_1.isdigit():
            op_1 = int(op_1) 
        elif op_1[0] in val_pos:
            op_1 = machine[op_1[0]][int(op_1[1])]
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif '-' in op_2:
            op_2 = int(op_2)
        elif op_2.isdigit():
            op_2 = int(op_2) 
        elif op_2[0] in val_pos:
            op_2 = machine[op_2[0]][int(op_2[1:])]

        if op_1 > op_2:
            if '-' in op_3:
                val = int(op_3)
                machine['s'] += val
                print(f"Status of the machine: \n\n{machine}\n\n")
                return execution(machine)
            elif i.isdigit():
                machine['s'] += int(i)
                print(f"Status of the machine: \n\n{machine}\n\n")
                return execution(machine)  
        else:
            machine['s'] += 1
            print(f"Status of the machine: \n\n{machine}\n\n")
            return execution(machine) 

    ###                                         HANDLING OF JLE (Jump to op_3 if op_& is strictly lesser than op_2)

    elif cmd == 'JLE':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)

        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]]
        op_2 = cmd_line[idx_vir[0]+1:idx_vir[1]] 
        op_3 = cmd_line[idx_vir[1]+1:idx_par[1]]

        if '@' in op_1:
            reg = op_1[:1]
            loc = op_1[2:]
            val = machine[loc[0]][int(loc[1])]
            op_1 = machine[reg][val]
        elif len(op_1) == 2:
            op_1 = machine[op_1[0]][int(op_1[1])]
        elif op_1.isdigit():
            op_1 = int(op_1) 
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            print(loc[0], loc[1])
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif len(op_2) == 2 and op_2.isdigit():
            op_2 = int(op_2)
        elif len(op_2) == 2 and op_2[0].isdigit() != True:
            op_2 = machine[op_2[0]][int(op_2[1])]
        elif len(op_2) == 1:
            op_2 = int(op_2)

        if op_1 < op_2:
            for i in op_3:
                if i == '-':
                    min = op_3.index('-')
                    val = int(op_3[min] + op_3[min+1])
                    machine['s'] = machine['s'] + val
                    print(f"Status of the machine: \n\n{machine}\n\n")
                    return execution(machine)
                elif i.isdigit():
                    machine['s'] += int(i)
                    print(f"Status of the machine: \n\n{machine}\n\n")
                    return execution(machine)  
        else:
            machine['s'] += 1
            print(f"Status of the machine: \n\n{machine}\n\n")
            return execution(machine)
    
    ###                                         HANDLING OF BRK (break)

    elif cmd == 'BRK':
        machine['o'][0] = len(machine['o']) -1
        print(f"Status of the machine: \n\n{machine}\n\n")
        return 'Congrats your code was executed with success !! feel free to notify all your friends'
    
    ###                                         ERROR HANDLING

    else: 
        raise(NameError(f"{cmd} not recognized, commands supported:\nADD\nSUB\nMLT\nDIV\nJMP\nJEQ\nJLA\nJLE\nBRK\n"))
    print(f"Status of the machine: \n\n{machine}\n\n")
    return execution(machine)

def parse_arguments():

    """
    Parses the command-line arguments.

    Returns:
    tuple: A tuple containing the file name and the input word for the RAM machine.
    """

    parser = argparse.ArgumentParser(description='Execute a RAM machine code.')
    parser.add_argument('file_name', type=str, help='Name of the RAM machine code file')
    parser.add_argument('word', type=int, nargs='+', help='Word of input data for the RAM machine')
    args = parser.parse_args()
    return args.file_name, args.word

def main():

    """
    Main function to execute the RAM machine code.
    """
     
    file_name, word = parse_arguments()
    program = read_RAM(file_name, word)
    message = execution(program)
    print(message)

if __name__ == "__main__":
    main()









