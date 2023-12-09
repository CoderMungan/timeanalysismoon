# timeanalysismoon

![GitHub](https://img.shields.io/github/license/CoderMungan/timeanalysismoon)

## Description
`timeanalysismoon` is a Python decorator that provides time analysis for Python functions. It measures and prints the execution time of a function.

## Installation
You can install `timeanalysismoon` using pip:

```bash
pip install timeanalysismoon
```

## Usage

```python
from timeanalysismoon import timeanalysismoon

@timeanalysismoon
def my_function():
    # Your function logic here
    pass

my_function()
```

## Example
Here's an example of how to use `timeanalysismoon`:

```python
from timeanalysismoon import timeanalysismoon

@timeanalysismoon
def example_function():
    for _ in range(1000000):
        pass

example_function()
```

### Author
- CoderMungan
    - Pypi.org: [https://pypi.org/project/timeanalysismoon/0.1/](https://pypi.org/project/timeanalysismoon/0.1/)
    - Email: codermungan@gmail.com
    - Github: [CoderMungan](https://github.com/CoderMungan)
