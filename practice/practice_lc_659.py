class Solution:

    def encode(self, strs):

        encode_str = ""
        for word in strs:
            encode_str += str(int(len(word))) + "&" + word

        return encode_str

    def decode(self, str):

        result = []
        i = 0
        while i < len(str) - 1:
            j = i

            while str[j] != "&":
                j += 1

            length = int(str[i:j])

            result.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return result


Input = ["lint", "code", "love", "you"]

print(Solution().encode(Input))

encode = Solution().encode(Input)

print(Solution().decode(encode))
