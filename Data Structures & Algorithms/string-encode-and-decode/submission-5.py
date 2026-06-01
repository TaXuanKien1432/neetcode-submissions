class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""

        for s in strs:
            for char in s:
                if char == "/":
                    encoded_s += "//"
                elif char == "-":
                    encoded_s += "/-"
                else:
                    encoded_s += char
            encoded_s += "-"
        
        return encoded_s

    def decode(self, s: str) -> List[str]:
        result = []
        decoded_s = ""
        i = 0

        while i < len(s):
            if s[i] == "-":
                result.append(decoded_s)
                decoded_s = ""
                i += 1
            elif s[i] == "/":
                if s[i+1] == "/":
                    decoded_s += "/"
                elif s[i+1] == "-":
                    decoded_s += "-"
                i += 2
            else:
                decoded_s += s[i]
                i += 1

        return result






