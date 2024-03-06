def longest_representation_length(t, S):
    n = len(t)
    F = [0] * (n + 1)
    # Filter out too long strings (longer than 't')
    S_cp = []
    for s in S:
        if len(s) <= n:
            S_cp.append(s)
    S = S_cp
    # Sort in order not to make unnecessary checks for too long strings
    S.sort(key=len)  # Bucket sort can be used
    
    for i in range(1, n + 1):
        j = 0
        # Check subsequent strings from the S array till they are no longer
        # than the current substring
        while j < len(S) and len(S[j]) <= i:
            substr = t[i - len(S[j]):i]
            if substr == S[j]:
                # If there is still some remaining part of a substring to check,
                # we have to assess whether the previous part has lower width
                # than the current one
                if i > len(substr):
                    F[i] = max(F[i], min(len(substr), F[i - len(substr)]))
                # If found a string of the same length as the current substring
                # and this substring is the whole substring we have already checked
                # (there are no other characters before this substring), we take this
                # substring as its representation ahs the largest width
                else:
                    F[i] = len(S[j])
                    break
            j += 1
        
    print(F)

    return F[n]
s1 = 'ab'
s2 = 'abab'
s3 = 'ba'
s4 = 'bab'
s5 = 'b'

S = [s1, s2, s3, s4, s5]
t = 'ababbab'
print(longest_representation_length(t, S))