# Currencies courses
currencies_to_usd = {'EUR': 0.85, 'UAH': 26.26, 'RUR': 62.13, 'GBP': 0.75, 'USD': 1}


def summ_in_usd(summ, currency):
    return float(summ) / currencies_to_usd[currency]


def sum_in_target_currency(summ_in_usd, target_currency):
    return float(summ_in_usd) * currencies_to_usd[target_currency]


# def input_string (currencies_to_usd):
#    for keys in currencies_to_usd:
#        print(keys + ', ', end='')

print('-' * 20)

while True:
    currency = input('Enter currency (EUR, UAH, RUR, GBP, USD):\n').upper()
    if currency not in currencies_to_usd:
        print('Invalid currency, try again')
    else:
        break

while True:
    try:
        summ = float(input('Enter summ:\n'))
    except ValueError:
        print('Invalid summ, try again')
    else:
        if summ <= 0:
            print('Invalid summ, try again')
        else:
            break

while True:
    target_currency = input('Enter target currency (EUR, UAH, RUR, GBP, USD):\n').upper()
    if target_currency not in currencies_to_usd:
        print('Invalid currency, try again')
    else:
        break

target_summ = sum_in_target_currency(summ_in_usd(summ, currency), target_currency)

print(summ, currency, '=', '{0:.2f}'.format(target_summ), target_currency)
print('-' * 20)
