# Description:
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Tags: Hash Table, Math
# Difficulty: Easy


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        prime = [True] * n
        count = n / 2

        for i in xrange(3, n, 2):
            if i * i >= n:
                break

            if not prime[i]:
                continue

            for j in xrange(i * i, n, i + i):
                if prime[j]:
                    prime[j] = False
                    count -= 1

        return count

    def countPrimes1(self, n):
        """
        Memory Limit Exceeded

        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        primes = set(xrange(3, n, 2))
        primes.add(2)

        i = 3
        while i * i < n:
            if i in primes:
                j = i * i
                while j < n:
                    primes.discard(j)
                    j += i + i
            i += 2

        return len(primes)
