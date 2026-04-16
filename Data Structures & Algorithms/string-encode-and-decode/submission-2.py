class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "$" + s

        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []

        while len(s) > 0:
            print("s is: " + s)
            str_size, s = s.split("$", 1)
            str_size = int(str_size)
            substr = s[0:str_size]
            if len(substr) != 0:
                _, s = s.split(substr, 1)
            strs.append(substr)

        return strs
