from typing import Union

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
            operation = elements[0][:-2] #récupère la ligne sans le caractère de retour à la ligne "\n"
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
    print("code initialized successfully\n")
    return program

# test de la fonction read_RAM:
ram = "text_to_be_read.txt"
program = read_RAM(ram, [5, 1, 15])
print(program)

# question 2 / 3 / 4
def execution(machine: dict):
    line_nb = machine ['s']
    cmd_line = machine['l'][line_nb]

    print("RAM execution status:\n")
    for key, value in machine['l'].items():
        if key == program["s"]:
            print(f"{value} <-- program is executing this step at the moment")
        else:
            print(f"{value}")
    print("\n")

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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
        elif op_2.isdigit():
            op_2 = int(op_2) 
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            print(reg, loc)
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 + op_2
            machine['s'] += 1
        elif len(op_3) > 1:
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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
        elif op_2.isdigit():
            op_2 = int(op_2) 
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][machine[loc[0]][int(loc[1])]] = op_1 - op_2
            machine['s'] += 1
        elif len(op_3) > 1:
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
        elif len(op_1) == 2:
            op_1 = machine[op_1[0]][int(op_1[1])]
        elif op_1.isdigit():
            op_1 = int(op_1) 
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
        elif op_2.isdigit():
            op_2 = int(op_2) 
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][machine[loc[0]][int(loc[1])]] = op_1 * op_2
            machine['s'] += 1
        elif len(op_3) > 1:
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

        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
        elif op_2.isdigit():
            op_2 = int(op_2) 
 
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][machine[loc[0]][int(loc[1])]] = round(op_1 / op_2, 2)
            machine['s'] += 1
        elif len(op_3) > 1:
            machine[op_3[0]][int(op_3[1])] = round(op_1 / op_2, 2)
            machine['s'] += 1

    elif cmd == 'JMP':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
        op = cmd_line[idx_par[0]+1:idx_par[1]]
        if '-' in op:
            machine['s'] += int(op)

    elif cmd == 'JEQ':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)

        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]] 
        op_2 = cmd_line[idx_vir[0]+1:idx_vir[1]]
        op_3 = cmd_line[idx_vir[1]+1:idx_par[1]]
        print(f"op2 status {op_2}")
        if '@' in op_1:
            reg = op_1[:1]
            loc = op_1[2:]
            val = machine[loc[0]][int(loc[1])]
            op_1 = machine[reg][val]
        elif len(op_1) == 2:
            op_1 = machine[op_1[0]][int(op_1[1])]
            print(f"status of op_1 {op_1}")
        elif len(op_1) == 1:
            op_1 = int(op_1) 
            
        if '@' in op_2:
            reg = op_2[:1]
            loc = op_2[2:]
            print(loc[0], loc[1])
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
        elif len(op_2) == 1:
            op_2 = int(op_2)
            print(f"op2 treated  {op_2}")

        if op_1 == op_2:
            for i in op_3:
                if i == '-':
                    min = op_3.index('-')
                    print(min)
                    val = int(op_3[min] + op_3[min+1])
                    machine['s'] = machine['s'] + val
                elif '-' not in op_3:
                    print(f"op3 not negative {op_3}")
                    machine['s'] += int(op_3)  
        else:
            machine['s'] += 1
            print("machine + 1")
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
            print(loc[0], loc[1])
            val = machine[loc[0]][int(loc[1])]
            op_2 = machine[reg][val]
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
        elif op_2.isdigit():
            op_2 = int(op_2)

        if op_1 > op_2:
            for i in op_3:
                if i == '-':
                    min = op_3.index('-')
                    print(min)
                    val = int(op_3[min] + op_3[min+1])
                    machine['s'] = machine['s'] + val
                elif i.isdigit():
                    machine['s'] += int(i)  
        else:
            machine['s'] += 1 
     
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
        elif len(op_2) == 2:
            op_2 = machine[op_2[0]][int(op_2[1])]
        elif op_2.isdigit():
            op_2 = int(op_2)

        if op_1 < op_2:
            for i in op_3:
                if i == '-':
                    min = op_3.index('-')
                    print(min)
                    val = int(op_3[min] + op_3[min+1])
                    machine['s'] = machine['s'] + val
                elif i.isdigit():
                    machine['s'] += int(i)  
        else:
            machine['s'] += 1
    
    elif cmd == 'BRK':
        return 'Congrats your code was executed with success !! feel free to notify all your friends'
    print(machine['s'], machine)
    return execution(machine)


print(execution(program))








