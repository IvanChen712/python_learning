def create_counter():
    x = 0

    def counter():
        nonlocal x
        x += 1
        return x

    return counter
