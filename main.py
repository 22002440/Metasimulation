from typing import Union
import argparse


# question 1
def read_RAM(file_name: any, word: Union[list, int]) -> dict:

    """
    Cette fonction permet de lire un fichier texte contenant le code
    d'une machine RAM et d'initialiser la structure de données
    pour représenter cette machine.

    """

    length_word = len(word)
    program = {}
    lin = {}  # dictionnaire pour les lignes
    inp = {0: length_word}  # dictionnaire pour les entrées
    reg = {}  # dictionnaire pour les registres
    out = {0: 0}  # dictionnaire pour les sorties
    stp = 0  # variable pour l'étape en cours

    with open(file_name, 'r') as file:
        lines = file.readlines()
        length_read = len(lines)
        for idx in range(length_read):
            # sépare les éléments de la ligne
            elements = lines[idx].strip().split()

            # prend la ligne sans '\n'
            operation = elements[0][:-2]

            # ajoute la ligne en cours au dictionnaire des lignes
            lin.update({idx: operation})
    for idx in range(1, length_word + 1):
        # ajoute les entrées au dictionnaire des entrées
        inp.update({idx: word[idx-1]})

    # ajout des lignes, entrées, registres, sorties et étapes au programme
    program["l"] = lin
    program["i"] = inp
    program["r"] = reg
    program["o"] = out
    program["s"] = stp

# affiche les éléments de la machine RAM
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


# question 2 / 3 / 4
def execution(machine: dict):

    """
    Execute les commandes de la machine RAM.

    Args:
    machine (dict): le dictionnaire représentant la machine RAM.

    Retourne:
    str: message de statut d'exécution.
    """
    # prend la ligne en cours d'exécution
    line_nb = machine['s']

    # prend la commande de la ligne en cours d'exécution
    cmd_line = machine['l'][line_nb]

    # affiche les éléments de la machine RAM en cours d'exécution
    print("RAM execution status:\n")
    for key, value in machine['l'].items():
        if key == machine["s"]:
            print(f"{value} <-- program is executing this step at the moment")
        else:
            print(f"{value}")
    print("\n")

    val_pos = ['i', 'r', 'o']  # liste des lettres possibles pour les registres
    idx_vir = []  # liste pour les virgules
    idx_par = []  # liste pour les parenthèses
    cmd = ''
    # prend les 3 premiers éléments de la ligne de commande
    for idx in range(3):
        cmd += cmd_line[idx]

    #                                        GESTION DE ADD (addition)

    #
    if cmd == 'ADD':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
            elif cmd_line[i] == ',':
                idx_vir.append(i)

        # op 1 à 3 sont les arguments de la ligne de commande,
        # on les récupère en faisant du slicing

        # op 2 est ce qui est entre ',' et ','
        op_2 = cmd_line[idx_vir[0]+1:idx_vir[1]]

        # op1 est ce qui est entre'(' et ',' op2 est ce qui est entre',' et ','
        op_1 = cmd_line[idx_par[0]+1:idx_vir[0]]

        # op 3 est ce qui est entre ',' et ')'
        op_3 = cmd_line[idx_vir[1]+1:idx_par[1]]

        # on parse chaque argument en vérifiant si il y a un '@'
        # si oui on prend ce qui est avant comme registre cible
        # et ce qui suit comme clé de l'index
        if '@' in op_1:
            reg = op_1[:1]
            loc = op_1[2:]
            val = machine[loc[0]][int(loc[1])]
            op_1 = machine[reg][val]

        # verifie si la valeur est négative, si elle l'est cela retourne faux
        # par exemple isdigit sur -4 retourne faux
        elif '-' in op_1:
            op_1 = int(op_1)

        elif op_1.isdigit():
            op_1 = int(op_1)

        # verifie si l'element à l'index 0 de op1
        # est l'une des lettres['i', 'r', 'o']
        elif op_1[0] in val_pos:
            op_1 = machine[op_1[0]][int(op_1[1])]

        # on fait la même chose pour op2
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

        # on fait la même chose pour op3
        if '@' in op_3:
            reg = op_3[:1]
            loc = op_3[2:]
            machine[reg][int(machine[loc[0]][int(loc[1])])] = op_1 + op_2
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1:])] = op_1 + op_2
            machine['s'] += 1

    #                                       GESTION DE SUB(soustraction)

    # on fait la même chose que ADD pour la commande SUB
    # seule l'opération change ici - avant +
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

    #                                         GESTION DE MLT (multiply)

    # même chose aussi, seule l'opération change ici * avant + et -
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

    #                                         GESTION DE DIV (division)

    # même chose encore, seule l'opération change ici / avant +, -, et *
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
            machine[reg][int(machine[loc[0]][int(loc[1])])] = round(
                op_1 / op_2, 2)
            machine['s'] += 1
        elif op_3[0] in val_pos:
            machine[op_3[0]][int(op_3[1])] = round(op_1 / op_2, 2)
            machine['s'] += 1

    #                                         GESTION DE JMP (Jump at arg)

    #  on deplace le pointeur de la machine avec la valeur de l'opérande
    elif cmd == 'JMP':
        for i in range(len(cmd_line)):
            if cmd_line[i] == '(' or cmd_line[i] == ')':
                idx_par.append(i)
        op = cmd_line[idx_par[0]+1:idx_par[1]]  # on prend l'opérande
        if '-' in op:  # si l'opérande est négatif
            # on ajoute la valeur de l'argument à la valeur de s
            machine['s'] += int(op)
            print(f"Status of the machine: \n\n{machine}\n\n")
            return execution(machine)
        else:  # même chose si l'opérande est positif
            machine['s'] += int(op)
            print(f"Status of the machine: \n\n{machine}\n\n")
            return execution(machine)

    #                   GESTION DE JEQ (sauter d' op_3 si op_1 est égal à op_2)

    # même principe que JMP, mais on saute de la valeur donnée si op1 == op2
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

    #   GESTION DE JLA (sauter à op_3 si op_1 est strictement supérieur à op_2)

    # même principe que JEQ, mais on saute de la valeur donnée si op1 > op2
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

    #  GESTION DE JLE (sauter à op_3 si op_1 est strictement inférieur à op_2)

    # même principe que JEQ, mais on saute de la valeur donnée si op1 < op2
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

    #                             GEESTION DE BRK(break)

    # on arrête l'exécution du programme si on rencontre BRK
    elif cmd == 'BRK':
        machine['o'][0] = len(machine['o']) - 1
        print(f"Status of the machine: \n\n{machine}\n\n")
        return 'Congrats your code was executed with success !! ' \
               'feel free to notify all your friends'

    #                              GESTION DES ERREURS

    # si la commande n'est pas reconnue, on lève une exception
    else:
        raise (NameError(f"{cmd} not recognized, commands supported:\n"
                         f"ADD\n"
                         f"SUB\n"
                         f"MLT\n"
                         f"DIV\n"
                         f"JMP\n"
                         f"JEQ\n"
                         f"JLA\n"
                         f"JLE\n"
                         f"BRK\n"))
    print(f"Status of the machine: \n\n{machine}\n\n")
    return execution(machine)


def parse_arguments():

    """
    Parse les arguments de la ligne de commande.

    Retourne:
    tuple: un tuple contenant le nom du fichier
    et le mot d'entrée pour la machine RAM.

    """

    parser = argparse.ArgumentParser(description='Execute a RAM machine code.')
    parser.add_argument('file_name',
                        type=str,
                        help='Name of the RAM machine code file')
    parser.add_argument('word',
                        type=int,
                        nargs='+',
                        help='Word of input data for the RAM machine')
    args = parser.parse_args()
    return args.file_name, args.word


def main():

    """
    Fonction principale pour exécuter le code de la machine RAM.

    """
    file_name, word = parse_arguments()
    program = read_RAM(file_name, word)
    message = execution(program)
    print(message)


if __name__ == "__main__":
    main()
