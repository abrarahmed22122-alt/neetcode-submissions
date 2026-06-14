class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decode_strs = []
        chars = iter(s)

        for char in chars:
            length_digits = ""
            while char != "#":
                length_digits += char
                char = next(chars)

            length = int(length_digits)
            word = "".join(next(chars) for i in range(length))
            decode_strs.append(word)
        return decode_strs

my_words = ["hello", "world"]

helper = Solution()

secret_code = helper.encode(my_words)
print("Encoded String:", secret_code)

original_words = helper.decode(secret_code)
print("Decoded List:  ", original_words)