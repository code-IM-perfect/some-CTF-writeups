
On reversing the binary it was clear what the answer to the initial 2 questions was and the third one did not have any right answer. All the inputs were being taken from `gets` so obviously there could be buffer overflows. The input from the last question was being saved starting from `rbp-0x3b` and the CMP statement was compairing `rbp-0x10` and `0xdea110c8`. So basically we had to input `0xdea110c8` after a buffer of `0x3b-0x10` which is 43, so the final payload was-
```py
payload=b'A'*43+p32(0xdea110c8)+b'\n'
```
