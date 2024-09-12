def eulerTour(n,adj,root):
    # flatten using euler tour
    # To store start and end times of nodes in DFS
    start = [-1] * n
    end = [-1] * n
    euler = []  # Flattened list of nodes in DFS order
    time = 0

    # Iterative DFS to avoid recursion depth issues
    stack = [(root, -1)]
    while stack:
        node, parent = stack.pop()
        if start[node] == -1:  # if node is not visited
            start[node] = time
            euler.append(node)
            time += 1
            stack.append((node, parent))  # Push back to handle end time
            for child in adj[node]:
                if child != parent:
                    stack.append((child, node))
        else:
            end[node] = time
    print(euler)


# Example:

from typing import List

from types import GeneratorType
from collections import defaultdict
# import sys

# sys.setrecursionlimit(10**5 + 50)

# recursion limit fix decorator, change 'return' to 'yield' and add 'yield' before calling the function
def bootstrap(f):
    stack = []

    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc

class SegmentTree:
    def __init__(self, arr, func=lambda x, y: x + y, default_value_func=lambda: 0):
        self.n = 1 << (len(arr) - 1).bit_length()
        self.func = func
        self.default_value_func = default_value_func
        self.segmentTree = [self.default_value_func() for _ in range(2 * self.n)]
        self.segmentTree[self.n : self.n + len(arr)] = arr
        for i in range(self.n - 1, 0, -1):
            self.segmentTree[i] = self.func(
                self.segmentTree[2 * i], self.segmentTree[2 * i + 1]
            )

    def query(self, l, r):
        l += self.n
        r += self.n
        resl = self.default_value_func()
        resr = self.default_value_func()
        while l < r:
            if l & 1:
                resl = self.func(resl, self.segmentTree[l])
                l += 1
            l >>= 1
            if r & 1:
                r -= 1
                resr = self.func(self.segmentTree[r], resr)
            r >>= 1
        return self.func(resl, resr)

    def update(self, i, value):
        i += self.n
        self.segmentTree[i] = value
        while i > 1:
            i >>= 1
            self.segmentTree[i] = self.func(
                self.segmentTree[2 * i], self.segmentTree[2 * i + 1]
            )

class Solution:
    def treeQueries(self, N : int, A : List[int], G : List[List[int]], Q : int, queries : List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for u,v in G :
            adj[u].append(v)
            adj[v].append(u)
        # flatten using euler tour
        # To store start and end times of nodes in DFS
        start = [-1] * N
        end = [-1] * N
        euler = []  # Flattened list of nodes in DFS order
        time = 0

        # Iterative DFS to avoid recursion depth issues
        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            if start[node] == -1:  # if node is not visited
                start[node] = time
                euler.append(node)
                time += 1
                stack.append((node, parent))  # Push back to handle end time
                for child in adj[node]:
                    if child != parent:
                        stack.append((child, node))
            else:
                end[node] = time
        # print(euler)

        segtree = SegmentTree([A[euler[i]] for i in range(N)], lambda x,y : (x*y) % MOD, lambda: 1)
        res = []
        for t,a,b in queries:
            if t == 1:
                segtree.update(start[a], b)
                res.append(-1)
            else:
                x = segtree.query(start[a],end[a])
                res.append(x)

        print(res)






#{
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        N = int(input())

        A = IntArray().Input(N)

        G = IntMatrix().Input(N - 1, 2)

        Q = int(input())

        queries = IntMatrix().Input(Q, 3)

        obj = Solution()
        res = obj.treeQueries(N, A, G, Q, queries)

        IntArray().Print(res)

# } Driver Code Ends