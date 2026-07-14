Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions will require a bit of explanation, not just a simple answer.

Q16: How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer:

A power of two has exactly one bit set (e.g. 1000 or 0100 — leading zeros
don't count). E.g. 0100 is 2^2 but 0110 is 2^2 + 2^1.

One method to figure this out is to repeatedly divide the number by 2:

Since 0 has no bits set and the power of 2 is always positive these are not checked. So, for any n > 0 , repeatedly right-shift n, which is equivalent to dividing by 2.
The bit dropped off by each shift is the remainder: if it's ever 1, n is not a
power of two. If you shift all the way down to a single remaining bit — the
original number's leading 1 — without ever dropping a 1, then n is a power of two.

Another, more efficient method is to check the bitwise AND of n with (n-1).

For example:

```
n = 1000
n-1 = 0111

n & (n - 1):
1000
0111
----
0000
```

If the result is 0000 then it is a power of two only if the result is 0.

Q17: If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: !

Q18: If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean? Answer:
Figure 2.2 illustrates 4 shades of gray, 0x00 = black, 0x55 = dark gray, 0xAA = light gray, and 0xFF = white. As 0x21 falls between black and dark gray, it would be classified as dark gray or very dark gray.

Q19: If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer:

```
AA = 10 * 16^1 + 10 * 16^0 = 170
00 = 0
FF = 0b11111111 = 2^8-1 = 255
```

Q20: If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer:

Red: 170

Green: 0

Blue: 255

A lot of blue and red = purple
