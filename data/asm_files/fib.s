.text

main:
   
    addi sp sp -4
    addi x11 x0 10
    
    addi sp sp -8
    sw ra 4(sp)
    sw x11 0(sp)
    call fib
    lw ra 4(sp)
    addi sp sp 8
    
    sw x10 0(sp)
    lw x11 0(sp)
    
    addi x10 x0 1
    ecall
    
    addi x10 x0 10
    ecall
    
fib:
    
    addi sp sp -8
    lw x10 8(sp) 
    addi x11 x0 1
    BGT x10 x11 rec 
    j return

rec: 
    
    lw x12 8(sp) 
    addi x12 x12 -1 # ertit naklebi
    
    addi sp sp -8  # x-1 is gamodzaxeba -------------
    sw ra 4(sp)
    sw x12 0(sp)
    call fib
    lw ra 4(sp)
    addi sp sp 8
    sw x10 4(sp)
    
    lw x12 8(sp) 
    addi x12 x12 -2
   
    addi sp sp -8   # x -2 is gamodzaxeba ------------
    sw ra 4(sp)
    sw x12 0(sp)
    call fib
    lw ra 4(sp)
    addi sp sp 8
    sw x10 0(sp)
    
    lw x11 4(sp)
    lw x10 0(sp)
    add x10 x10 x11
    
return:
   
   addi sp sp 8
   ret


    
    
    
    
    
    
    
    
    