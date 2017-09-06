# -*- coding: utf-8 -*-


def replace_space(raw_str, new):
    # count query
    tar = ' '
    cnt = raw_str.count(tar)
    diff = len(new) - len(tar)
    postfix = ['0']*cnt*diff
    new_str = raw_str + postfix
    print new_str
    j = len(new_str) - 1
    i = len(raw_str) - 1
    while j>=0:
        if new_str[j] == tar:
            for k in range(len(new))[::-1]:
                new_str[j] =  new_str[k]
                j -= 1
        else:
            new_str[j] = new_str[i]
            i -= 1
            j -= 1
    return new_str









if __name__ == '__main__':
    raw_str = "We are happy."
    raw_str = list(raw_str)
    print replace_space(raw_str, "%20")
