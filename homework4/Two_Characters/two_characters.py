def twoCharacters(s):
    unique_chars = list(set(s))
    max_len = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            c1 = unique_chars[i]
            c2 = unique_chars[j]

            # keep only two characters
            filtered = [ch for ch in s if ch == c1 or ch == c2]

            # check alternating
            valid = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k + 1]:
                    valid = False
                    break

            if valid:
                max_len = max(max_len, len(filtered))

    return max_len