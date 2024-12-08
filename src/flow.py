""" method process commands
parsing through the list of assembly lines we remove 
space characters and make a list containing list of commands
"""
def process_commands(curr_cpu):
    index = 0
    for line in curr_cpu.commands:
        parts = line.strip().split()
        if not parts:
            continue  # Skip empty lines
        
        curr_cpu.commands[index] = parts
        index += 1;


def labels(curr_cpu):
    for i, line in enumerate(curr_cpu.commands):

        if line[0].endswith(":"):
            curr_cpu.label_ind.append((line[0][:-1],i))
        elif ":" in line:
            curr_cpu.label_ind.append((line[0],i))            
        