li x10 -300
addi x11 x11, -153
addi sp, sp, -8
sw x10, 0(sp)
sw x11, 4(sp)
call min
addi sp, sp, 8
addi   x10, x0, 1
add x11, x0 , x20
ecall
addi x10, x0, 10
ecall

min:
lw x10, 0(sp)
lw x11, 4(sp)
bge x10, x11, else
lw x20, 0(sp)
ret
else:
lw x20, 4(sp)
ret