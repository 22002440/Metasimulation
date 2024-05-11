# Dm_Metasimulation 
# README

## Description

Ce programme Python permet d'exécuter le code d'une machine RAM (Random Access Machine) à partir d'un fichier texte contenant le code de la machine et une entrée spécifiée.
Il est spécifié dans le code à quelle question correspond chaque partie.
Concercant la question 5, ce sont les fichiers .txt joints qui y répondent et pour vérifier leurs fonctionnements suivez les étapes indiquées dans la partie utilisation.

## Utilisation

1. Assurez-vous d'avoir Python installé sur votre système.
2. Ouvrez un terminal.
3. Placez-vous dans le répertoire où se trouve le fichier `main.py` et le fichier de la machine RAM.
4. Exécutez le programme en utilisant la commande suivante :

    ```bash
    python main.py la_machine_ram.txt input
    ```

    Remplacez `la_machine_ram.txt` par le nom de votre fichier contenant le code de la machine RAM et `input` par les entrées que vous souhaitez fournir à la machine.
    Pour la question 5 les fichiers sont : a_power_b.txt et bubble_sort.txt.
    Utilisez l'entrée que vous voulez, pour le premier donnez d'abord a 'espace' b, pour le second donnez chaque nombre du tableau un par un, ils sont tous séparés d'un espace.

    

## Format du fichier de la machine RAM

Le fichier de la machine RAM doit contenir le code de la machine, où chaque ligne représente une instruction. Les instructions supportées sont :

- `ADD`: Addition
- `SUB`: Soustraction
- `MLT`: Multiplication
- `DIV`: Division
- `JMP`: Sauter à l'adresse spécifiée
- `JEQ`: Sauter si égal à
- `JLA`: Sauter si supérieur à
- `JLE`: Sauter si inférieur à
- `BRK`: Arrêter l'exécution

## Contributeurs
Malak LALAMI 22000319
Naoufal AMALLAH 22002440