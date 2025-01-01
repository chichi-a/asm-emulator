
addi x12 x12 10
li x13 444
addi sp sp -8
sw x12 0(sp)
sw x13 4(sp)

# address of num in x13
addi x15 sp 4

# print adress of num in x13
add x11 x0 x15
li x10 1
ecall

# write value of num in x13 in x15
lw x15 0(x15)
add x11 x0 x15
li x10 1
ecall

li x10 10
ecall