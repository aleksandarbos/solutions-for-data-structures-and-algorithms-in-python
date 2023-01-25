

def clear(s):
    if len(s) == 0:
        return
    s.pop()
    clear(s)

if __name__ == "__main__":
    s = ['A', 'l', 'e', 'k', 's', 'a', 'n', 'd', 'a', 'r']
    print(f'before cleaning, len(s): {len(s)}')
    assert len(s) == 10

    clear(s)

    print(f'after cleaning, len(s): {len(s)}')
    assert len(s) == 0
