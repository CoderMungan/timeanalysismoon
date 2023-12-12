# timeanalysismoon

![GitHub](https://img.shields.io/github/license/CoderMungan/timeanalysismoon)

## Overview

Welcome to version 0.5 of the `timeanalysismoon` Python package! This release introduces a decorator designed to measure and print the execution time of functions, providing a simple and effective way to profile your Python code.

## Key Features

- **Decorator Functionality**: The `timeanalysismoon` decorator, when applied to a function, calculates the time it takes for the function to run and prints the result.

- **Ease of Use**: Integrating the decorator into your code is straightforward. Simply apply `@timeanalysismoon` above the function you want to analyze.

## Example Usage

```python
from timeanalysismoon.decorator import timeanalysismoon

@timeanalysismoon
def example_function():
    # Your function logic here
    pass
```
## Installation

You can install the package using the following pip command:

```bash
pip install timeanalysismoon
```
or

```bash
pip install timeanalysismoon==0.7
```

## Compatibility
- Supports Python 3.6 to 3.12

## Release Notes
- **Enhancement**: Improved performance in certain scenarios.
- **Bug Fix**: Fixed a minor issue related to time calculation precision.

## How to Contribute

If you have any suggestions, improvements, or bug reports, feel free to contribute to the project by opening issues or submitting pull requests on the [GitHub repository](https://github.com/CoderMungan/timeanalysismoon).

## License

This package is released under the MIT License. See the [LICENSE](https://github.com/CoderMungan/timeanalysismoon/blob/main/license) file for details.

### Author
- CoderMungan
    - Pypi.org: [https://pypi.org/project/timeanalysismoon/0.7/](https://pypi.org/project/timeanalysismoon/0.7/)
    - Email: codermungan@gmail.com
    - Github: [CoderMungan](https://github.com/CoderMungan)
