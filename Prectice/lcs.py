from functools import lru_cache


def lcs(str1, str2):
    """Return the length of the longest common subsequence."""
    @lru_cache(maxsize=None)
    def length(first_index, second_index):
        if first_index == len(str1) or second_index == len(str2):
            return 0
        if str1[first_index] == str2[second_index]:
            return 1 + length(first_index + 1, second_index + 1)
        return max(
            length(first_index + 1, second_index),
            length(first_index, second_index + 1),
        )

    return length(0, 0)


if __name__ == "__main__":
    print(lcs("bhaskar", "askar"))