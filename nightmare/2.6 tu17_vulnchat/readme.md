
Okay so this was a bit tricky. We have 2 buffer overflows, both having a read size of 30 but having a buffer size of 20. I thought `%30s` would only affect the strings smaller than 30, but apparently it crops out the overflowing part. But the lucky thing is that `%30s` isn't hardcoded and is stored in a variable at `[rbp-0x5]` which comes in the overflowing region of our first input which begins at `[rbp-0x19]`. The offset between these locations is `0x19-0x5` which is 20 (also cuz the first buffer was 20 and no other variable was stored in between). So basically our first input should be something like(90 is completely arbitrary)-
```py
payload1=b'A'*20+b'%90s'
```
The second input starts from `[rbp-0x2d]` and the return address is stored at `[rbp+0x4]` (from IDA, which makes sense because there is no canary) so the second offset is `0x2d+0x4` which is 49 (This is smaller than our arbitrarily picked buffer of 90 so there is no problem). The address of printFlag function is `0x0804856B`. So our final payload would look like-
```py
payload2=b'A'*49+p32(0x0804856B)
```
and it works!!!
