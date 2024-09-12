def solve1():
    def lps(pat):
        m = len(pat)
        l=[0]*m
        length,i=0,1
        while i < m:
            if pat[i] == pat[length]:
                l[i] = length+1
                length+=1
                i+=1
            else:
                if length>0:
                    length=l[length-1]
                else:
                    i += 1
        return l
    def search(pat, txt):
        lps1 = lps(pat)
        ans = []
        i,j=0,0
        #rint(lps)
        while i < len(txt):
            if txt[i] == pat[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps1[j-1]
                else:
                    i+=1
            if j == len(pat):
                ans.append(i-j+1)
                j = lps1[j-1]

        return ans
    text,pattern = input(), input()
    print(len(search(txt=text, pat=pattern)))