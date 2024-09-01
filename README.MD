# Argparse Example Script
This Python script demonstrates how to use the `argparse` module for parsing command-line arguments. It handles inputs for a first name, family name, and age, and provides customized output based on the provided arguments. \
## Features:
- Accepts `-n` or `--name` for the first name.
- Accepts `-f` or `--family` for the family name.
- Accepts `-a` or `--age` for the age.
- Outputs a formatted string based on the provided arguments.
## Usage:
To run the script, use the following command:
```
python main.py -n <first_name> -f <family_name> -a <age>
```
Replace `<first_name>`, `<family_name>`, and `<age>` with your actual values. You can omit any of these options to see how the script responds.
```commandline
python main.py -n John -f Doe -a 30
```
### Output:
```commandline
I am John Doe, I am 30 years old.
```
Feel free to adjust the details to better fit your script or any additional information you want to provide!