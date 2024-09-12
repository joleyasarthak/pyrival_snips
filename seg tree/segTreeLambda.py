from typing import List
from types import GeneratorType
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

# first lambda: aggregation function used by the segment tree
# second lambda: This is the default value function. eg addition me 0, mul me 1
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

# Example Code
class Solution:
    def treeQueries(self, N : int, A : List[int], G : List[List[int]], Q : int, queries : List[List[int]]) -> List[int]:

        tree = [[] for _ in range(N)]
        for u, v in G:
            tree[u].append(v)
            tree[v].append(u)

        position_map = {}
        end_map = {}
        traversal = []

        @bootstrap
        def dfs(u, p):
            position_map[u] = len(traversal)
            traversal.append(u)

            for v in tree[u]:
                if v == p:
                    continue
                yield dfs(v, u)

            end_map[u] = len(traversal)
            yield

        MOD = 10**9 + 7
        dfs(0, -1)
        tree = None

        segtree = SegmentTree([A[i] for i in traversal], lambda x, y: (x * y) % MOD, lambda: 1)
        ans = [-1] * Q
        for i in range(Q):
            if queries[i][0] == 1:
                segtree.update(position_map[queries[i][1]], queries[i][2])
            else:
                ans[i] = segtree.query(position_map[queries[i][1]], end_map[queries[i][1]])

        return ans


