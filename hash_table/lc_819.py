class Solution:
    def mostCommonWord(self,paragraph, banned):
        # Step 1: Normalize text - lowercase and extract words
        words = re.findall(r'\w+', paragraph.lower())

        print(words)

        # Step 2: Convert banned list to a set for quick lookup
        banned_set = set(banned)

        print(banned_set)
        # Step 3: Manually count word frequencies
        freq = {}
        for word in words:
            if word not in banned_set:
                freq[word] = freq.get(word, 0) + 1

        # Step 4: Find the word with the highest frequency
        most_common = ""
        max_count = 0
        for word, count in freq.items():
            if count > max_count:
                most_common = word
                max_count = count

        return most_common
