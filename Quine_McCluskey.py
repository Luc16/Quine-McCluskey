import script_input
# import terminal_input
idx_order = []
difference = 0
difference_idx = 0
new_additions = 0
matched_variables = []
new_var = []
new_truth_table = []
final_truth_table = []
nvar = terminal_input.args.nvar


def outing_to_truth_table(array):
    _truth_table = []
    for i in range(len(array)):
        if array[i] == 1:
            digit = [int(digit) for digit in bin(i)[2:].zfill(nvar)]
            _truth_table.append(digit)
    return _truth_table


def handle_input(input_table, input_outing):
    if input_table == '0':
        h_input = list(map(int, input_outing.split()))
        return outing_to_truth_table(h_input)
    elif input_outing == '0':
        h_input = []
        [h_input.append(list(map(int, i))) for i in input_table.split()]
        return h_input


if __name__ == "__main__":
    truth_table = handle_input(script_input.input_table, script_input.input_outing)
    # truth_table = handle_input(terminal_input.args.input_table, terminal_input.args.input_outing)
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
    print(final_truth_table)
