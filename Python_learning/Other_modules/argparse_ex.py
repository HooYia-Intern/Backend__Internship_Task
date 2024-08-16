import argparse

# Create argument parser
parser = argparse.ArgumentParser(description='Sample argparse script.')
parser.add_argument('number', type=int, help='A number to be processed')
args = parser.parse_args()

print(f"Number provided: {args.number}")
