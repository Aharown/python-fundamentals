# # Suppose that you’d like to implement a cookie jar in which to store cookies.
# In a file called jar.py, implement a class called Jar with these methods:

# # __init__ should initialize a cookie jar with the given capacity, which represents
# the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int,
# though, __init__ should instead raise a ValueError.

# # __str__ should return a str with 𝑛 🍪, where 𝑛 is the number of cookies in the cookie jar.
# For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
# # deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity,
# though, deposit should instead raise a ValueError.

# # withdraw should remove n cookies from the cookie jar. Nom nom nom.
# If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
# # capacity should return the cookie jar’s capacity.
# # size should return the number of cookies actually in the cookie jar, initially 0.
# # Structure your class per the below. You may not alter these methods’ parameters, but you may add your own methods.


#pseudcode
# __init__(self, capacity=12)
# validate capacity is a non-negative using isinstance
# if not raise ValueError
# assign capacity to self._capacity (private) remember _ makes it priv
# assign self._size to 0 (private)

# __str__(self)
# return cookie emoji multiplied by self._size
# deposit(self, n)
# if self._size + n exceeds self._capacity raise ValueError
# else increment self._size by n
# withdraw(self, n)
# if n exceeds self._size raise ValueError
# else decrement self._size by n

# @property capacity(self)
# return self._capacity

# @property size(self)
# return self._size

# Time: O(1) all operations are constant regardless of jar size
# Space: O(1) fixed number of instance variables


class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Not enough space in jar")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies in jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


if __name__ == "__main__":
    jar = Jar()
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(1)
    print(jar)
