from timeanalysismoon import timeanalysismoon

def main():
    @timeanalysismoon
    def example_function():
        print("Example function is running!")

    example_function()

if __name__ == "__main__":
    main()