def move(n, source, auxiliary, target):
    if n == 1:
        print(f"{source} --> {target}")
    else:
        move(n - 1, source, target, auxiliary)
        print(f"{source} --> {target}")
        move(n - 1, auxiliary, source, target)


# Example usage
move(5, 'A', 'B', 'C')
