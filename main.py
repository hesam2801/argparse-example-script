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
