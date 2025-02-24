
def generator_example(n):
    for i in range(n):
        yield i * i

for value in generator_example(5):
    print(value)
