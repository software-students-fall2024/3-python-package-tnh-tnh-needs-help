# Python Package Exercise: ASCII ZOO

[![Run Moo Test](https://github.com/software-students-fall2024/3-python-package-tnh-tnh-needs-help/actions/workflows/test_one.yaml/badge.svg)](https://github.com/software-students-fall2024/3-python-package-tnh-tnh-needs-help/actions/workflows/test_one.yaml)
[![Run input_parse_test](https://github.com/software-students-fall2024/3-python-package-tnh-tnh-needs-help/actions/workflows/test_two.yaml/badge.svg)](https://github.com/software-students-fall2024/3-python-package-tnh-tnh-needs-help/actions/workflows/test_two.yaml)
[![Run wrong_test](https://github.com/software-students-fall2024/3-python-package-tnh-tnh-needs-help/actions/workflows/test_three.yaml/badge.svg?v=1)](https://github.com/software-students-fall2024/3-python-package-tnh-tnh-needs-help/actions/workflows/test_three.yaml)
[![Run get_noise_test](https://github.com/software-students-fall2024/3-python-package-tnh-tnh-needs-help/actions/workflows/test_four.yaml/badge.svg)](https://github.com/software-students-fall2024/3-python-package-tnh-tnh-needs-help/actions/workflows/test_four.yaml)

## Project Description

ASCII ZOO is a small silly python package that prints ASCII animal art based on certain user inputs. Watch out for the interrupting cow... (It appears randomly).

ASCII Zoo allows you to:

1. **Print Art Animal**: Displays ASCII art of the animal along with its name.
2. **Animal Sounds**: Outputs the corresponding sound after printing the ASCII animal.
3. **Surprise Cow**: Randomly shows up with an ASCII art representation and a “moo”.
4. **Wrong Output**: Handles unrecognized animal names, confirming wrong input with a playful response.

## Example Code

```py
from ascii_art_TNH import ascii_art

ascii_art("cat dog") # Will print one cat and one dog

ascii_art("woof") # Will print one dog
```

## How this package was created

```sh
.
├── .github
│   └── workflows
│       ├── test_one.yaml
│       ├── test_two.yaml
│       ├── test_three.yaml
│       └── test_four.yaml
├── src
│   └── ascii_art_TNH
│       ├── __init__.py
│       ├── __main__.py
│       ├── ascii_art.py
│       ├── gallery.py
│       └── noises.py
├── tests
│   ├── __init__.py
│   ├── input_parse_test.py
│   ├── moo_test.py
│   ├── wrong_input_test.py
│   └── get_noise_test.py
├── .gitignore
├── README.md
├── pyproject.toml
└── requirements.txt
```

## How to install and use this package

### Prerequisites

- **Python** (version 3.6 or later)
- **pip** (Python package installer)
- **pipenv** (for managing virtual environments)

### Installation

You can find our package on PyPI: [Ascii_Art_TNH](https://pypi.org/project/Ascii_Art_TNH/)

To install the package, use pip:

```sh
pip install Ascii_Art_TNH
```

## How to run unit tests

Test are included within the 'test' directory. To run these test...

1. Install pytest in a virtual enviorment
2. Run the test from the main project directory:

```sh
python3 -m pytest
```

## How to contribute

Clone the repository

```sh
git clone https://github.com/software-students-fall2024/3-python-package-tnh-tnh-needs-help.git
cd 3-python-package-tnh-tnh-needs-help
```

Set up the virtual environment and install any dependencies

```sh
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```

Build and test the package

```sh
python -m build
python -m pytest
```

## Continuous integration

This project uses a continuous integration workflow that builds and runs unit tests automatically with every _push_ of the code to GitHub.

## Team Members

[Hugo](https://github.com/BringoJr)\
[Nuzhat](https://github.com/ntb5562)\
[Melanie](https://github.com/melanie-y-zhang)\
[Tamara](https://github.com/TamaraBuenoo)
