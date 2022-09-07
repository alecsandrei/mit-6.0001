# source: https://www.youtube.com/watch?v=_o4T-ChIYC8

def positions(char, word_list):
    ext_lst = []
    output_lst = []
    for elem in word_list:
        ext_lst.append(list(elem))
    for lst in ext_lst:
        for i in range(len(lst) + 1):
            lst.insert(i, char)
            output_lst.append("".join(lst))
            lst.remove(char)
    return output_lst


def get_permutations(sequence):
    if len(sequence) == 1:
        return list(sequence)
    return positions(sequence[0], get_permutations(sequence[1::]))
