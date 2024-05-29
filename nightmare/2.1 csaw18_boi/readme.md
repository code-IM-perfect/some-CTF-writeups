# CSAW18 boi

Flag: NA

There is a `CMP` operation which compares `eax` to `0xcaf3baee`. After taking input and before CMP, `0xdeadbeef` is loaded to `eax`. Also there is a buffer overflow (just exact lol) in the read function. We can use the buffer overflow to overwrite `0xdeadbeef` with `0xcaf3baee` (effectively `eax`)

I found the offset by using `cyclic` and `cyclic_find` from pwntools and finally used this payload-
```py
payload = b'A'*20+p64(0xcaf3baee)
```
I have included the exact script in this folder.
