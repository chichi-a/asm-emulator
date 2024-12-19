add x12 x13 x14
addi  x10 x10, 30
adDI x11 x11, -15
addi sp, sp, -8
sw x10, 0(sp)
sw x11, 4(sp)  # fagagaga
#blaablaaa
call min
addi sp, sp, 8
addi   x10, x0, 1
mv   x11, x20
jump else
ecall
li x10, 10
ecall

min :
lw x10, 0(sp)
lw x11, 4(sp)
jump else
bge x10, x11, else
lw x20, 0(sp)
ret
else:
lw x20, 4(sp)
ret