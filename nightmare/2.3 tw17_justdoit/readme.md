
We were asked for a password input, the password was in plain sight on reversing but it was recording the `\n` too because of fgets and CMP was comparing without `\n` so I had to use- `io.sendline(b'P@SSW0RD'+b'\x00')` to stop fgets at the null character. But the password check was not doing anything important, it turned out that the `flag.txt` was being opened via `fopen` and the contents were later being stored in `flag` which was located from `.bss:0804A080` to `.bss:0804A0AF` so basically 48 characters. Locally from gdb I could just read from that memory location, but obviously the challenge was made for a binary on the server, so I used another vulnerability to print it. The fail/success message was being loaded to eax and then written to `[ebp-0xc]` and later this was being read and was getting printed via `puts`. We could overwrite stuff at `[ebp-0xc]` by the pointer to the flag array `0804A080`, this would result in the flag being printed.

Our input was being saved at `[ebp-0x20]`, so we needed to have an offset of `0x20-0xc` which is 20, so the final payload was-
```py
payload = b'A'*20 + p32(0x0804a080)
```
