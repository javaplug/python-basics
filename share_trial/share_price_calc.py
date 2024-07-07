import share_trial.csv_reader as reader

shares = reader.read_csv('shareData.csv', [str, str, int, float])
total_share_price = 0.0
for share in shares:
    print(share)
    total_share_price += share['shares'] * share['price']
print('Total share price : ', total_share_price)
