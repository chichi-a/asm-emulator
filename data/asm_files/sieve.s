 
addi x10, x0, 1   
addi x13, x0, 103

addi x12,x0,0 #count of primes so far
addi x14,x0,2 #curr num

prime:
    bgt x14, x13 prime_end
    addi x15,x0,0 #checker
    addi x16,x0,0 #j (s[j] is a prime num we already found)

    for_j:
        bge x16,x12, for_j_end
            addi x19, x0, 4
            mul x17, x16, x19     # 2 3 5 7 
            add x18, x17, sp
            lw x18, 0(x18)
            rem x18, x14, x18
            beq x18, zero, if_non_prime
            addi, x16, x16, 1

        j for_j 

    if_non_prime:
        addi x15, x15, 1

    for_j_end :

    bne x15, zero, N_add_prime
    addi sp, sp, -4
    sw x14, 0(sp)
    addi x12, x12, 1

    lw  x11, 0(sp) 
    #printing
    ecall

    N_add_prime:
        addi x15, zero, 0
        addi x14, x14, 1
        addi x16, x0, 0
        j prime

prime_end:
    li x10, 10
    ecall