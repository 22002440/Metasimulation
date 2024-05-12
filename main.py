from typing import Union
import argparse

# question 1
def read_RAM(file_name: any, word: Union[list, int]) -> dict:
    """
    Cette fonction permet de lire un fichier texte contenant le code
    d'une machine RAM et un mot d'entrée et d'initialiser
    la structure de données pour représenter cette machine.
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
            operation = elements[0] 
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





# question 2
def next_step(machine: dict):
    line_nb = machine ['s']
    cmd_line = machine['l'][line_nb]
    
    print("\nRAM execution status before next step:\n")
    for key, value in machine['l'].items():
        if key == machine["s"]:
            print(f"{value} <-- program is executing this step at the moment")
        else:
            print(f"{value}")
    print("\n")
    print(f"Status of the machine before next step: \n\n{machine}\n\n")
    val_pos = ['i', 'r', 'o']
    idx_at = []
    idx_vir = []
    idx_par = []
    cmd = ''
    for idx in range(3):
        cmd += cmd_line[idx]
        
    if cmd == 'ADD':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)

        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]] # +1 parcequ'on veut les valeurs après le premier idx dans le slicing 
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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 + op_2
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = op_1 + op_2
            machine['s'] += 1

    elif cmd == 'SUB':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)
        
        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]] # +1 parcequ'on veut les valeurs après le premier idx dans le slicing 
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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 - op_2
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = op_1 - op_2
            machine['s'] += 1

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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 * op_2
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = op_1 * op_2
            machine['s'] += 1

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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = round(op_1 / op_2, 2)
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = round(op_1 / op_2, 2)
            machine['s'] += 1

    elif cmd == 'JMP':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
        op = cmd_line[idx_par[0]+1:idx_par[1]]
        if '-' in op:
            machine['s'] += int(op)
            print("\nRAM execution status after next step:\n")
            for key, value in machine['l'].items():
                if key == machine["s"]:
                    print(f"{value} <-- program is executing this step at the moment")
                else:
                    print(f"{value}")
            print("\n")
            print(f"Status of the machine after next step: \n\n{machine}\n\n")
        else:
            machine['s'] += int(op)
            print("\nRAM execution status after next step:\n")
            for key, value in machine['l'].items():
                if key == machine["s"]:
                    print(f"{value} <-- program is executing this step at the moment")
                else:
                    print(f"{value}")
            print("\n")
            print(f"Status of the machine after next step: \n\n{machine}\n\n")
        
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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]

        if op_1 == op_2:
            for i in op_3:
                if i == '-':
                    min = op_3.index('-')
                    val = int(op_3)
                    machine['s'] = machine['s'] + val
                    
                    print("\nRAM execution status after next step:\n")
                    for key, value in machine['l'].items():
                        if key == machine["s"]:
                            print(f"{value} <-- program is executing this step at the moment")
                        else:
                            print(f"{value}")
                    print("\n")
                    print(f"Status of the machine after next step: \n\n{machine}\n\n")

                elif '-' not in op_3:
                    machine['s'] += int(op_3)
                    print("\nRAM execution status after next step:\n")
                    for key, value in machine['l'].items():
                        if key == machine["s"]:
                            print(f"{value} <-- program is executing this step at the moment")
                        else:
                            print(f"{value}")
                    print("\n")
                    print(f"Status of the machine after next step: \n\n{machine}\n\n") 
        else:
            machine['s'] += 1
            print("\nRAM execution status after next step:\n")
            for key, value in machine['l'].items():
                if key == machine["s"]:
                    print(f"{value} <-- program is executing this step at the moment")
                else:
                    print(f"{value}")
            print("\n")
            print(f"Status of the machine after next step: \n\n{machine}\n\n")
        
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
        elif len(op_1) == 2:
            op_1 = machine[op_1[0]][int(op_1[1])]
        elif op_1.isdigit():
            op_1 = int(op_1) 
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif len(op_2) == 2 and op_2.isdigit():
            op_2 = int(op_2)
        elif len(op_2) == 2 and op_2[0].isdigit() != True:
            op_2 = machine[op_2[0]][int(op_2[1])]
        elif len(op_2) == 1:
            op_2 = int(op_2)

        if op_1 > op_2:
            for i in op_3:
                if i == '-':
                    min = op_3.index('-')
                    val = int(op_3[min] + op_3[min+1])
                    machine['s'] += val
                    print("\nRAM execution status after next step:\n")
                    for key, value in machine['l'].items():
                        if key == machine["s"]:
                            print(f"{value} <-- program is executing this step at the moment")
                        else:
                            print(f"{value}")
                    print("\n")
                    print(f"Status of the machine after next step: \n\n{machine}\n\n")

                elif i.isdigit():
                    machine['s'] += int(i)
                    print("\nRAM execution status after next step:\n")
                    for key, value in machine['l'].items():
                        if key == machine["s"]:
                            print(f"{value} <-- program is executing this step at the moment")
                        else:
                            print(f"{value}")
                    print("\n")
                    print(f"Status of the machine after next step: \n\n{machine}\n\n") 
        else:
            machine['s'] += 1
            print("\nRAM execution status after next step:\n")
            for key, value in machine['l'].items():
                if key == machine["s"]:
                    print(f"{value} <-- program is executing this step at the moment")
                else:
                    print(f"{value}")
            print("\n")
            print(f"Status of the machine after next step: \n\n{machine}\n\n") 
        
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
                    print("\nRAM execution status after next step:\n")
                    for key, value in machine['l'].items():
                        if key == machine["s"]:
                            print(f"{value} <-- program is executing this step at the moment")
                        else:
                            print(f"{value}")
                    print("\n")
                    print(f"Status of the machine after next step: \n\n{machine}\n\n")

                elif i.isdigit():
                    machine['s'] += int(i)
                    print("\nRAM execution status after next step:\n")
                    for key, value in machine['l'].items():
                        if key == machine["s"]:
                            print(f"{value} <-- program is executing this step at the moment")
                        else:
                            print(f"{value}")
                    print("\n")
                    print(f"Status of the machine after next step: \n\n{machine}\n\n")  
        else:
            machine['s'] += 1
            print("\nRAM execution status after next step:\n")
            for key, value in machine['l'].items():
                if key == machine["s"]:
                    print(f"{value} <-- program is executing this step at the moment")
                else:
                    print(f"{value}")
            print("\n")
            print(f"Status of the machine after next step: \n\n{machine}\n\n")
    elif cmd == 'BRK':
        machine['o'][0] = len(machine['o']) -1
        print(f"Status of the machine after next step: \n\n{machine}\n\n")
        return 'Congrats your code was executed with success !! feel free to notify all your friends', machine
    else:
        raise(NameError(f"{cmd} not recognized, commands supported:\nADD\nSUB\nMLT\nDIV\nJMP\nJEQ\nJLA\nJLE\nBRK\n"))
    print("\nRAM execution status after next step:\n")
    for key, value in machine['l'].items():
        if key == machine["s"]:
            print(f"{value} <-- program is executing this step at the moment")
        else:
            print(f"{value}")
    print("\n")
    print(f"Status of the machine after next step: \n\n{machine}\n\n")
    return machine





# question 3 / 4
def execution(machine: dict):
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
        
    if cmd == 'ADD':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)

        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]] # +1 parcequ'on veut les valeurs après le premier idx dans le slicing 
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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 + op_2
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = op_1 + op_2
            machine['s'] += 1

    elif cmd == 'SUB':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)
        
        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]] # +1 parcequ'on veut les valeurs après le premier idx dans le slicing 
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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 - op_2
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = op_1 - op_2
            machine['s'] += 1

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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 * op_2
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = op_1 * op_2
            machine['s'] += 1

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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = round(op_1 / op_2, 2)
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = round(op_1 / op_2, 2)
            machine['s'] += 1

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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]

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
        elif len(op_1) == 2:
            op_1 = machine[op_1[0]][int(op_1[1])]
        elif op_1.isdigit():
            op_1 = int(op_1) 
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif len(op_2) == 2 and op_2.isdigit():
            op_2 = int(op_2)
        elif len(op_2) == 2 and op_2[0].isdigit() != True:
            op_2 = machine[op_2[0]][int(op_2[1])]
        elif len(op_2) == 1:
            op_2 = int(op_2)

        if op_1 > op_2:
            for i in op_3:
                if i == '-':
                    min = op_3.index('-')
                    val = int(op_3[min] + op_3[min+1])
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
    elif cmd == 'BRK':
        machine['o'][0] = len(machine['o']) -1
        print(f"Status of the machine: \n\n{machine}\n\n")
        return 'Congrats your code was executed with success !! feel free to notify all your friends', machine
    else:
        raise(NameError(f"{cmd} not recognized, commands supported:\nADD\nSUB\nMLT\nDIV\nJMP\nJEQ\nJLA\nJLE\nBRK\n"))
    print(f"Status of the machine: \n\n{machine}\n\n")
    return execution(machine)





#question 8
def graph_oriente(machine:dict):
    graph = {'n': {},
             'e': {},
             'm': []
            }


    for idx, instruction in machine['l'].items():
        graph['n'].update({idx:instruction})


    for _ in range(len(graph['n'])):
        graph['m'] = [[0]* len(machine["l"]) for _ in range(len(machine['l']))]

    idx_edge = 0
    for idx, instruction in machine['l'].items():
        operation = instruction[:3]
        idx_par = [i for i in range(len(instruction)) if instruction[i] == '(' or instruction[i] == ')']
        idx_vir = [i for i in range(len(instruction)) if instruction[i] == ',']
        if operation in ['ADD', 'SUB', 'MLT', 'DIV', 'JMP']:
            if operation == 'JMP':
                target = int(instruction[idx_par[0]+1:idx_par[1]]) 
                graph['e'].update({idx_edge:(idx, idx + target)})
                idx_edge += 1
            else:
                next_instruction = idx + 1
                graph['e'].update({idx:(idx, next_instruction)})
                idx_edge += 1
        elif operation in ['JEQ', 'JLA', 'JLE']:
            target = int(instruction[idx_vir[1]+1:idx_par[1]])
            graph['e'].update({idx_edge:(idx, idx + target)})
            next_instruction = idx + 1
            graph['e'].update({idx_edge + 1:(idx, next_instruction)})
            idx_edge += 2
        elif operation == 'BRK':
            # BRK instruction ends the program
            break

        for edge in graph['e'].values():
            graph['m'][edge[0]][edge[1]] = 1
    return graph

#question 9
def dfs(graph, start, visited):
    """
    Depth-first search function to traverse the graph from the given start node.

    Args:
    - graph (dict): The graph containing nodes, edges, and adjacency matrix.
    - start (int): The index of the start node.
    - visited (list): A list to keep track of visited nodes.

    Returns:
    - None
    """
    visited[start] = True
    print(f"Visiting node {start}: {graph['n'][start]}")

    for neighbor, connected in enumerate(graph['m'][start]):
        if connected and not visited[neighbor]:
            dfs(graph, neighbor, visited)

def traverse_and_mark_unreachable(graph: dict):
    """
    Traverse the graph from the first node to the last node, marking unreachable nodes.

    Args:
    - graph (dict): The graph containing nodes, edges, and adjacency matrix.

    Returns:
    - unreachable (list): The list of instruction unreachable.
    """
    print(graph)
    num_nodes = len(graph['n'])
    visited = [False] * num_nodes
    unreachable = []
    # Perform DFS from the first node
    dfs(graph, 0, visited)

    # Mark unreachable nodes as inaccessible
    for idx, node in enumerate(visited):
        if not node:
            unreachable.append(idx)
            print(f"Node {idx} is unreachable and marked inaccessible.")
    return unreachable
    

def opti_ram(target_file:str, unreachable: list, machine:dict):
    operation = {}
    operation_opti = {}
    size = len(operation)
    
    if unreachable == []:
        return "everything is fine lol"
     
    with open(target_file, 'r') as file:
            lines = file.readlines()
            lenth_read = len(lines)
            for idx in range(lenth_read):
                elements = lines[idx].strip().split()
                operation.update({idx:elements[0]}) #récupère la ligne sans le caractère de retour à la ligne "\n"

    for idx, instruction in operation.items():
        if idx not in unreachable:
            operation_opti.update({idx: instruction})
    
    with open(f'{target_file[:-4] + '_opti.txt'}', 'w') as file :
        for _, instruction in operation_opti.items():
            line = instruction
            if line == 'BRK':
                file.write(f"{line}")
            else:
                file.write(f"{line}\n")

            
# automatisation du code par commande dans le terminal

def parse_arguments():
    parser = argparse.ArgumentParser(description='Execute a RAM machine code.')
    parser.add_argument('file_name', type=str, help='Name of the RAM machine code file')
    parser.add_argument('word', type=int, nargs='+', help='Word of input data for the RAM machine')
    parser.add_argument('mode', type=str, help='Mode of execution supported modes: opti or default or matrix or step')
    args = parser.parse_args()
    return args.file_name, args.word, args.mode

def main():
    file_name, word, mode = parse_arguments()
    program = read_RAM(file_name, word)
    if mode == 'opti':
        tree = graph_oriente(program)
        unreachable = traverse_and_mark_unreachable(tree)
        message = opti_ram(file_name,unreachable,program)
    elif mode == 'default':
        message = execution(program)
    elif mode == 'matrix':
        tree = graph_oriente(program)
        message = tree['m']
    elif mode == 'step':
        config_1 = {'l': {0: 'ADD(i0,0,r0)', 1: 'ADD(i@r0,0,r1)', 2: 'SUB(r0,1,r0)', 3: 'ADD(i@r0,r1,r1)'
                          , 4: 'SUB(r0,1,r0)', 5: 'JEQ(r0,0,2)', 6: 'JMP(-3)', 7: 'ADD(i0,0,r0)'
                          , 8: 'DIV(r1,i0,r1)', 9: 'ADD(r1,0,o1)', 10: 'BRK'}
                          , 'i': {0: 5, 1: 2, 2: 5, 3: 56, 4: 42, 5: 166}
                          , 'r': {0: 5, 1: 271}, 'o': {0: 0}, 's': 8}
        
        config_2 = {'l': {0: 'ADD(i0,0,r0)', 1: 'ADD(i@r0,0,r1)', 2: 'SUB(r0,1,r0)'
                          , 3: 'ADD(i@r0,r1,r1)'
                          , 4: 'SUB(r0,1,r0)', 5: 'JEQ(r0,0,2)', 6: 'JMP(-3)', 7: 'ADD(i0,0,r0)'
                          , 8: 'DIV(r1,i0,r1)', 9: 'ADD(r1,0,o1)', 10: 'BRK'}
                          , 'i': {0: 5, 1: 2, 2: 5, 3: 56, 4: 42, 5: 166}, 'r': {0: 1, 1: 269}
                          , 'o': {0: 0}, 's': 3}
        
        config_3 = {'l': {0: 'ADD(i0,0,r0)', 1: 'ADD(i@r0,0,r1)', 2: 'SUB(r0,1,r0)'
                          , 3: 'ADD(i@r0,r1,r1)', 4: 'SUB(r0,1,r0)', 5: 'JEQ(r0,0,2)'
                          , 6: 'JMP(-3)', 7: 'ADD(i0,0,r0)', 8: 'DIV(r1,i0,r1)', 9: 'ADD(r1,0,o1)'
                          , 10: 'BRK'}, 'i': {0: 5, 1: 2, 2: 5, 3: 56, 4: 42, 5: 166}
                          , 'r': {0: 5, 1: 54.2}, 'o': {0: 0}, 's': 9}
        
        message = next_step(config_3)
    else:
        raise(ValueError("Mode entered is not supported expected --> opti or default or test or step"))
    print(message)

if __name__ == "__main__":
    main()