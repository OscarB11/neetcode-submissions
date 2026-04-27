from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_dict = {}
        print("Input strings:", strs)

        for i in strs:
            # Create a key by sorting the string (or use Counter for more flexibility)
            ana = tuple(sorted(i))  # Sorting gives a unique key for anagrams
            print(f"String '{i}' sorted gives key: {ana}")

            if ana not in anagrams_dict:
                anagrams_dict[ana] = []
                print(f"New key '{ana}' added to dictionary.")

            anagrams_dict[ana].append(i)
            print(f"Adding '{i}' to group of anagrams with key '{ana}'. Current groups: {anagrams_dict}")

        # Return all values from the dictionary as grouped anagrams
        result = list(anagrams_dict.values())
        print("Final grouped anagrams:", result)
        return result

