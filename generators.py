"""S.NO.	YIELD	RETURN
1	Yield is generally used to convert a regular Python function into a generator. | Return is generally used for the end of the execution and “returns” the result to the caller statement.
2	It replace the return of a function to suspend its execution without destroying local variables.  |  It exits from a function and handing back a value to its caller.
3	It is used when the generator returns an intermediate result to the caller. | 	It is used when a function is ready to send a value.
4	Code written after yield statement execute in next function call.	 |  while, code written after return statement wont execute.
5	It can run multiple times.	| It only runs single time.
6	Yield statement function is executed from the last state from where the function get paused. |  Every function calls run the function from the start.
"""


def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for num in genfibon(20):
    print(num)


s = "hello"
# Iterate over string
for let in s:
    print(let)

try:
    next(s)
except TypeError:
    print("TypeError occurred")
s_iter = iter(s)
print(next(s_iter))
