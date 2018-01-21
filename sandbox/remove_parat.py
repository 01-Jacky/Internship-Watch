def remove_paranthesis(s):
    index = s.find('(')
    if index == -1:
        return s
    else:
        return s[:index]


print(remove_paranthesis('los angeles, CA (somewhere nice)'))