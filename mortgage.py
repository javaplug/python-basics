
import math

principle = 500000
payment = 30300
rate = 10.5
period = 5
interest_per_year = 12
total_paid = 0

month = 0
while principle > 0:
    month += 1
    interest = principle * (rate/100) * period / 12
    principle = principle + interest - payment
    total_paid += payment
    print('{:>10d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month, interest, total_paid - interest, principle))

print('%10.2f paid in %3d years %2d months' % (total_paid, month/12, (month%12)))

