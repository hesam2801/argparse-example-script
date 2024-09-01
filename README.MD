# Argparse Example Script
Command-line argument parsing is a fundamental skill in Python programming, enabling developers to create scripts that are flexible and user-friendly. The argparse module, part of Python's standard library, provides a powerful and intuitive way to handle command-line arguments. In this article, we’ll explore a practical example of using argparse through a simple Python script.

Introduction to argparse
The argparse module is designed to handle command-line arguments for your Python scripts. It allows you to specify what arguments your script expects, parse those arguments when the script runs, and provide helpful error messages when the user provides invalid input.

Example Script Overview
In our example, we have a Python script that demonstrates the use of argparse to parse command-line arguments related to a person's name and age. The script will format and display a message based on the provided arguments.

Here’s the script:
```python
import argparse

parser = argparse.ArgumentParser(description='Example script.', allow_abbrev=False)

parser.add_argument('-n', '--name', type=str, help='Your first name.')
parser.add_argument('-f', '--family', type=str, help='Your family.')
parser.add_argument('-a', '--age', type=int, help='Your age.')

try:
    args = parser.parse_args()
except SystemExit:
    print("Invalid command")
    exit()

output = (
    f'I am {args.name} {args.family}, I am {args.age} years old.' if args.name and args.family and args.age else
    f'I am {args.name} {args.family}.' if args.name and args.family and not args.age else
    f'I am {args.name}.' if args.name and not args.family and not args.age else
    f'I am {args.age} years old.' if not args.name and not args.family and args.age else
    f'I am {args.family}.' if not args.name and args.family and not args.age else 'Invalid command')

print(output)

```
## Features:
- Accepts `-n` or `--name` for the first name.
- Accepts `-f` or `--family` for the family name.
- Accepts `-a` or `--age` for the age.
- Outputs a formatted string based on the provided arguments.
## How It Works
1. #### ArgumentParser Initialization:
```python
parser = argparse.ArgumentParser(description='Example script.', allow_abbrev=False)
```
The ArgumentParser object is created with a description of the script. The allow_abbrev=False parameter ensures that arguments must be specified fully and not abbreviated.
2. #### Adding Arguments:
```python
parser.add_argument('-n', '--name', type=str, help='Your first name.')
parser.add_argument('-f', '--family', type=str, help='Your family name.')
parser.add_argument('-a', '--age', type=int, help='Your age.')
```
We define three optional arguments: `--name`, `--family`, and `--age`. Each argument is associated with a help description and type.
3. #### Parsing Arguments:
```python
try:
    args = parser.parse_args()
except SystemExit:
    print("Invalid command")
    exit()
```
We use `parse_args()` to process command-line inputs. If invalid arguments are provided, a `SystemExit` exception is caught, and an error message is printed.
4. #### Generating Output:
```python
output = (
    f'I am {args.name} {args.family}, I am {args.age} years old.' if args.name and args.family and args.age else
    f'I am {args.name} {args.family}.' if args.name and args.family and not args.age else
    f'I am {args.name}.' if args.name and not args.family and not args.age else
    f'I am {args.age} years old.' if not args.name and not args.family and args.age else
    f'I am {args.family}.' if not args.name and args.family and not args.age else 'Invalid command')
```
The script constructs an output message based on which arguments are provided. It handles various cases to generate a suitable message or an "Invalid command" response.
## Running the Script:
To run the script, use the following command:
```
python main.py -n <first_name> -f <family_name> -a <age>
```
Replace `<first_name>`, `<family_name>`, and `<age>` with your actual values. You can omit any of these options to see how the script responds.
```commandline
python main.py -n Hesam -f Alavi -a 23
```
### Output:
```commandline
I am Hesam Alavi, I am 23 years old.
```
Feel free to adjust the details to better fit your script or any additional information you want to provide!
# Conclusion
The `argparse` module is a versatile tool for managing command-line inputs, providing users with clear error messages and flexible argument handling. This example script demonstrates the basic usage of argparse, showcasing how to set up arguments, handle errors, and produce customized output based on user input.

By mastering `argparse`, you can make your Python scripts more robust and user-friendly, offering a better experience for those who run your programs from the command line.