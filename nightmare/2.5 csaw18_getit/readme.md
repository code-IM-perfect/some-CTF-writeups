
On decompiling I found the helpfully named `give_shell` function. We obviously need to run this function located at `0x4005b6`. We can do this by exploiting the buffer overflow from the `gets` function (literally had it in the name)

I calculated the offset-to-the-return to be 40 via `cyclic` and `cyclic_find`, so the final payload should have been-
```py
payload=b'A'*40+p64(0x4005b6)
```
But again this does not work for me locally, maybe this would have worked on the deployed server cuz all the writeups for this also effectively do this itself.
### DOES NOT WORK for me locally
