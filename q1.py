def findContentChildren(g, s):
    g.sort()  # kids
    s.sort()  # cookies
    no_of_kids = len(g)
    no_of_cookie = len(s)
    content = 0
    j = 0

    while content < no_of_kids and j < no_of_cookie:
        if s[j] >= g[content]:
            content += 1
        j += 1
    return content


g = [1, 4, 2]
s = [1, 2, 3]

print(f'The number of content children is {findContentChildren(g, s)}')

g = [1, 2, 3]
s = [3]
print(f'The number of content children is {findContentChildren(g, s)}')
