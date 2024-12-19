valid_registerr = [5,6,7,10,11,12,13,14,15,16,17,28,29,30,31]


class CPU:

    def __init__(self):
        """ in this list each index represents one byte of stack/heap
        """
        self.memory_blocks = [0]*10001  
        # what offset of stack are we currently on
        self.curr_offset_pointer = 10000;
        self.total_size = 10001

        """here we save 32 registers, where some of them can be
        alletred by thi caller
        x0 is default zero
        x1 is return address
        x2 is stack pointer, pointing to current address on memory block 
        """
        self.registers = [0,0,10000,"gp","tp"]
        self.registers.extend([None] * (33 - len(self.registers)))

        for i in valid_registerr:
            self.registers[i] = 0

        """
        list where we save assembly line commands
        """
        self.commands = []

        self.label_ind = {}