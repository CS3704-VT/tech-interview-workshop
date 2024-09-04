class Solution(object):
    def reverseVowels(self, s):
        # have the pointers move across the word. one from the front to the end and the other from the end to the front. Stop when the end pointer is less than the front pointer
        front = 1
        end = len(s)-1
        inp = list(s)
        vowels = "AEIOUaeiou"

        while front < end:
                # find vowel from start
                while front < end and vowels.find(inp[front])==-1:
                    front+=1

                # find vowel from end
                while front < end and vowels.find(inp[end])==-1:
                    end+=-1
                
                # when vowels found swap them
                temp = inp[end]
                inp[end] = inp[front]
                inp[front] = temp

                front+=1
                end-=1

        return inp
