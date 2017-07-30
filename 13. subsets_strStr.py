class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        if len(target) == 0:
            return 0

        idx = -1
        for i in range(len(source) - len(target) + 1):
            pos = i
            for j in range(len(target)):
                if target[j] == source[pos]:
                    pos += 1
                else:
                    break
            if j == pos - i - 1:
                return i
        return -1
