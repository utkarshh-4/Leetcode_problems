class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anag={}

        for word in strs :
            key=''.join(sorted(word))

            if key not in anag:
                anag[key]=[]

            anag[key].append(word)

        return list(anag.values())

        