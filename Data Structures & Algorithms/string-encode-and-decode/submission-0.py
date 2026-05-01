class Solution:
    def pad_num(self, num: int, width: int = 4, char: str = "#") -> str:
        s = str(num)
        padding_needed = width - len(s)
        if padding_needed <= 0:
            return s
        return char * padding_needed + s

    def parse_pad(self, s: List[str], char: str = "#") -> int:
        if not s:
            return 0
        i = 0
        n = len(s)

        while i < n and s[i] == char:
            i += 1

        num = 0
        while i < n:
            c = s[i]
            num = num * 10 + (ord(c) - ord("0"))
            i += 1

        return num

    def encode(self, strs: List[str]) -> str:
        code = []

        for s in strs:
            n = len(s)
            code.append(self.pad_num(n) + s)

        return "".join(code)

    def decode(self, s: str) -> List[str]:
        strs = []
        n = len(s)
        i = 0
        while i < n:
            code = []
            while len(code) != 4:
                code.append(s[i])
                i += 1
            num = self.parse_pad(code)
            l = i + num
            val = []
            while i < l and i < n:
                val.append(s[i])
                i+=1

            strs.append("".join(val))
        return strs
