import argparse

parser = argparse.ArgumentParser(
    description='''"First type the number of variables.
    Then type an outing or the truth tables ones.
    For the table output write in the format '1 0 1 0 1 0 1 0'
    For the truth table write in the format '000 001 010'"''')
parser.add_argument('nvar', type=int, default=0, help='Number of variables')
parser.add_argument('input_table_output', type=str, default='0', help='If you want to input the truth table output')
parser.add_argument('input_table', type=str, default='0', help='If you want to input the truth table ones')
args = parser.parse_args()
