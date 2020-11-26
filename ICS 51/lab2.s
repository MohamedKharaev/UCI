#                                           ICS 51, Lab #2
# 
#                                          IMPORTATNT NOTES:
# 
#                       Write your assembly code only in the marked blocks.
# 
#                     DO NOT change anything outside the marked blocks.
# 
#                      Remember to fill in your name, student ID in the designated sections.
# 
#

###############################################################
#                           Data Section
.data
# 
# Fill in your name, student ID in the designated sections.
# 
student_name: .asciiz "Mohamed Kharaev"
student_id: .asciiz "43121144"

new_line: .asciiz "\n"
space: .asciiz " "
gets: .asciiz " -> "
testing_label: .asciiz "Testing "
strlen_label: .asciiz "Strlen \n"
valid_id_label: .asciiz "Valid ID \n"

num_tests: .word 4
test_1: .asciiz ""
test_2: .asciiz "Ca$h"
test_3: .asciiz "[Ca$h]"
test_4: .asciiz "{CASH}_R...ules_ever23ythi*ng ar( )ound me!."
input_data:
    .word test_1, test_2, test_3, test_4
test_1_out: .space 100
test_2_out: .space 100
test_3_out: .space 100
test_4_out: .space 100
output_data:
    .word test_1_out, test_2_out, test_3_out, test_4_out
###############################################################
#                           Text Section
.text

#                          Main Function

main:

li $v0, 4
la $a0, student_name
syscall
la $a0, new_line
syscall  
la $a0, student_id
syscall 
la $a0, new_line
syscall

test_strlen:
lw $s1, num_tests
li $s0, 0
li $v0, 4
la $a0, testing_label
syscall
la $a0, strlen_label
syscall 

test1_loop:
beq $s0, $s1, test_valid_id

la $t0, input_data
sll $a0, $s0, 2
add $t0, $t0, $a0
lw $a0, ($t0)

sub $sp,$sp,4
sw $a0,($sp)

jal strlen

lw $a0,($sp)
addiu $sp,$sp,4

move $t0, $v0
li $v0, 4
syscall
la $a0, gets
syscall  

move $a0, $t0
li $v0, 1
syscall 
li $v0, 4
la $a0, new_line
syscall

addi $s0, $s0, 1
b test1_loop

test_valid_id:

li $v0, 4
la $a0, new_line
syscall
lw $s1, num_tests
li $s0, 0
li $v0, 4
la $a0, testing_label
syscall
la $a0, valid_id_label
syscall 

test2_loop:
beq $s0, $s1, end

la $t0, input_data
la $t1, output_data

sll $a0, $s0, 2
add $t0, $t0, $a0
lw $a0, ($t0)
sll $a1, $s0, 2
add $a1, $t1, $a1
lw $a1, ($t1)

sub $sp,$sp,4
sw $a0,($sp)
sub $sp,$sp,4
sw $a1,($sp)

jal valid_id

lw $a1,($sp)
addiu $sp,$sp,4
lw $a0,($sp)
addiu $sp,$sp,4

li $v0, 4
syscall
la $a0, gets
syscall 
move $a0, $a1 
syscall 

li $v0, 4
la $a0, new_line
syscall

addi $s0, $s0, 1
b test2_loop

end:
# end program
li $v0, 10
syscall


###############################################################
###############################################################
###############################################################
#                            PART 1 (Strlen)
# You are given a null-terminated strings ($a0). You need calculate its length and store in ($v0).
# Basically you should count number of characters before reaaching the character with value of 0.
# int strlen (str) {
#    int len = 0;
#    while (str[len] != 0)   // 0 != '0'
#        len++;
#    return len;
# }
		
############################## Part 1: your code begins here ###
strlen:
move $v0, $zero
BeginningOfWhile:
	lb $t1, 0($a0)
	beqz $t1, EndOfWhile
	addi $a0, $a0, 1
	addi $v0, $v0, 1
j BeginningOfWhile
EndOfWhile:
############################## Part 1: your code ends here   ###
jr $ra
###############################################################
#                           PART 2 (Valid IDs)
#
# Takes a null terminated (C-Style) string and returns another C-style string only
# containing valid characters. Valid characters are defined to be alphanumeric characters (a-A,b-B,0-9)
# and "_" (underscore) character.
# $a0 : pointer to input string buffer
# $a1 : pointer to output string buffer (initially all zeros)
valid_id:
############################### Part 2: your code begins here ##
### [48-57] [65-90] [95] [97-122] 
	
WhileLoop:
	lb $t1, 0($a0)
	beq $t1, $zero, EndLoop
	addi $a0, $a0, 1

	beq $t1, 95, alphanumeric

	blt $t1, 47, WhileLoop
	bgt $t1, 122, WhileLoop

	blt $t1, 58, alphanumeric
	bgt $t1, 96, alphanumeric

	blt $t1, 65, WhileLoop
	bgt $t1, 90, WhileLoop

alphanumeric:

	sb $t1, ($a1)
	addi $a1, $a1, 1
	
	j WhileLoop

EndLoop:

############################### Part 2: your code ends here  ##
jr $ra
