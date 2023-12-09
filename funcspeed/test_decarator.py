from decarator import timeanalysismoon

@timeanalysismoon
def example_function():
    for _ in range(1000000):
        pass

example_function()
