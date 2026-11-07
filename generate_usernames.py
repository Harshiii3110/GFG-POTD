class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        # code here
        reserved = set(arr)
        used = set()
        next_suffix = {}
        result = []

        for name in arr:
            if name not in used:
                result.append(name)
                used.add(name)
            else:
                suffix = next_suffix.get(name, 1)

                while name + str(suffix) in reserved or name + str(suffix) in used:
                    suffix += 1

                new_name = name + str(suffix)

                result.append(new_name)
                used.add(new_name)
                next_suffix[name] = suffix + 1

        return result
