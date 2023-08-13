def generate_pascals_triangle():
    row_ = [1]
    yield row_
    while True:
        next_row = [1]
        for i in range(1, len(row_)):
            next_row.append(row_[i - 1] + row_[i])
        next_row.append(1)
        row_ = next_row
        yield row_


# Example usage
triangle_generator = generate_pascals_triangle()
for _ in range(10):
    row = next(triangle_generator)
    print(row)
