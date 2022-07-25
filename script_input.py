import Quine_McCluskey as qm

if __name__ == '__main__':
    initial_string = "First type the number of variables.\nThen type an outing or the truth tables ones.\nFor the outing write in the format '1 0 1 0 1 0 1 0'\nFor the truth table write in the format '000 001 010'"
    print(initial_string)
    nvar = int(input("Input number of variables: "))
    input_table_output = str(input("(If you don't want this kind of input type enter) Input table output : "))
    input_table = str(input("(If you don't want this kind of input type enter) Input truth table with in a single line : "))
    input_1 = qm.handle_input(nvar, input_table, input_table_output)
    quine = qm.quine_mccluskey(nvar, input_1)
    print(qm.num_to_letter(nvar, quine))
