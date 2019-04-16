"""

Given a string, you need to reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not
be any extra space in the string.

"""

class Solution:
    def reverseWordsOfString(self, s):
        print(s)
        s = s.split(" ")
        new_word = ""
        for word in s:
            letters = [char for char in word]
            rev_word = []
            for c in word:
                rev_word.append(letters.pop())
            new_word += ("".join(rev_word)) + " "
        return(new_word.rstrip())
