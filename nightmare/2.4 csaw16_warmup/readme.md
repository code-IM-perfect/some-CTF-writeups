
On decompiling it is obvious that we need to run the `easy` function. Even though there is no PIE and so the address of easy should remain the same, the program is printing out the address to the function. Using recieve until, I was also getting `\n` so I trimmed it out and converted it from string to int
```py
addr=int(io.recvuntil('\n')[:-1].decode(),16)
```
Then I calculated the offset-to-the-return to be 72 via `cyclic` and `cyclic_find`, so the final payload should have been-
```py
payload=b'A'*72+p64(addr)+b'\n'
```
But I struggled with this a lot and this does not work, the nightmare solution says that for some env the offset could be 0x40 instead of 0x48 for some setups (did not elaborate why) but that doesn't work either
### DOES NOT WORK
