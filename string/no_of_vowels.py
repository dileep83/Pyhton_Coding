# Count the Number of Vowel Strings in Range
class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        vowels = {"a","e","i","o","u"}
        number_of_vowel_strings = 0
        for i in range(left ,right+1):
            if (words[i][0] in vowels) and (words[i][-1] in vowels) :   # String can be treated as a matrix or n-d array
                number_of_vowel_strings+=1
        return number_of_vowel_strings

if __name__ == "__main__":
    s = Solution()
    print(s.vowelStrings(["hello","leetcode","ae","iou","qr","wet"], 0, 5))
    print((2+3)//2)