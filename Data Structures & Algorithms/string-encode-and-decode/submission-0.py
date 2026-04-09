class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
           
            encoded_str += str(len(s)) + '#' + s
        
  
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s):
            # i would want to start finding the index # starting from i 
            j = s.find('#', i)
            # then i would grab the length size of the word
            length = int(s[i:j])

            #then i want to append the word
            #to do that i would need to know the index of the start and end of the word
            start = j + 1
            end = start + length

            #append
            decoded_str.append(s[start:end])

            #then ill go to the next word
            i = end



        return decoded_str