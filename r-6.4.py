s = ['A', 'l', 'e', 'k', 's', 'a', 'n', 'd', 'a', 'r']


def clear(s):
    if len(s) == 0:
        return
    s.pop()
    clear(s)

print(f'before cleaning, len(s): {len(s)}')

clear(s)

print(f'after cleaning, len(s): {len(s)}')
