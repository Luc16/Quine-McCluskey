#import script_input
# import terminal_input


def outing_to_truth_table(nvar, array):
    _truth_table = []
    for i in range(len(array)):
        if array[i] == 1:
            digit = [int(digit) for digit in bin(i)[2:].zfill(nvar)]
            _truth_table.append(digit)
    return _truth_table


def handle_input(nvar, input_table, input_table_output):
    if input_table == '0':
        h_input = list(map(int, input_table_output.split()))
        return outing_to_truth_table(nvar, h_input)
    elif input_table_output == '0':
        h_input = []
        [h_input.append(list(map(int, i))) for i in input_table.split()]
        return h_input


def num_to_letter(nvar, final_array):
    letter_array = []
    final_string = ""
    j_appended = 0
    for letter in range(65, 65+nvar):
        letter_array.append(chr(letter))
    for i in range(len(final_array)):
        for j in range(nvar):
            if final_array[i][j] == 1:
                if j_appended != 0:
                    final_string += "."
                final_string += letter_array[j]
                j_appended += 1
            elif final_array[i][j] == 0:
                if j_appended != 0:
                    final_string += "."
                final_string = final_string+"|"+letter_array[j]
                j_appended += 1
        j_appended = 0
        if i != (len(final_array) - 1):
            final_string += " + "
    return final_string


# truth_table = handle_input(script_input.input_table, script_input.input_table_output)
def quine_mccluskey(nvar, truth_table):
    idx_order = []
    difference = 0
    difference_idx = 0
    new_additions = 0
    matched_variables = []
    new_var = []
    new_truth_table = []
    final_truth_table = []
    while True:
        idx_order = [[sum(i), truth_table.index(i)] for i in truth_table]
        for i in range(len(idx_order)):
            for j in range(1, (len(idx_order)-i)):
                if idx_order[i+j][0] == (idx_order[i][0] + 1):
                    for k in range(nvar):
                        if truth_table[idx_order[i][1]][k] != truth_table[idx_order[i+j][1]][k]:
                            difference += 1
                            difference_idx = k
                            if difference > 1:
                                break
                    if difference == 1:
                        new_additions += 1
                        new_var = list(truth_table[i])
                        new_var[difference_idx] = 2
                        matched_variables.append(truth_table[idx_order[i + j][1]])
                        if new_var not in new_truth_table:
                            new_truth_table.append(new_var)
                    difference = 0
                elif idx_order[i+j][0] > (idx_order[i][0] + 1):
                    break
            if (new_additions == 0) and (truth_table[i] not in matched_variables):
                final_truth_table.append(truth_table[i])
            new_additions = 0
        if truth_table == new_truth_table:
            break
        truth_table = new_truth_table
        new_truth_table = []

    return final_truth_table


if __name__ == "__main__":
    nvar = 2
    _to = [0, 1, 0, 1]
    tt = [[0, 1], [1, 1]]
    to = outing_to_truth_table(nvar, _to)
    qm = quine_mccluskey(nvar, tt)
    print(num_to_letter(nvar, qm))
