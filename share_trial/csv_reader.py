import csv


def read_csv(file_name, types):
    shares_file = open(file_name, 'r')
    rows = csv.reader(shares_file)
    header = next(rows)
    shares = []
    for rowNum, row in enumerate(rows, start=1):
        try:
            row = [func(val) for func, val in zip(types, row)]
        except ValueError as err:
            print('Bad row ', rowNum, ' : ', row, ' reason : ', err)
            continue # Skips bad row
        shares.append(dict(zip(header, row)))
    return shares
