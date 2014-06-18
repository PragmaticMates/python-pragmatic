def round_to_n_decimal_places(value, n):
    power = 10 ** n
    return float(int(value * power)) / power
