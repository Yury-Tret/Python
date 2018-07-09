# Currencies courses
currencies = {'EUR': 0.85, 'UAH': 26.26, 'RUR': 62.13, 'GBP': 0.75, 'USD': 1}


class Converter:

    def __init__(self, currencies_to_usd):
        self.exit_flag = False
        self.currencies_to_usd = currencies_to_usd

    def summ_in_usd(self, summ, currency):
        return float(summ) / self.currencies_to_usd[currency]

    def sum_in_target_currency(self, summ_in_usd, target_currency):
        return float(summ_in_usd) * self.currencies_to_usd[target_currency]

    def calculate(self):
        target_summ = self.sum_in_target_currency(self.summ_in_usd(self.summ, self.currency), self.target_currency)
        print(self.summ, self.currency, '=', '{0:.2f}'.format(target_summ), self.target_currency)
        print('-' * 20)
        while True:
            exit_flag = input('Do you want exit?: [Y/n]')
            if exit_flag == 'Y'.lower():
                self.exit_flag = True
                return
            elif exit_flag == 'n':
                self.exit_flag = False
                return
            else:
                print('Non existent choice, try again')

    def input(self):

        print('-' * 20)

        while True:
            self.currency = input('Enter currency (EUR, UAH, RUR, GBP, USD):\n').upper()
            if self.currency not in self.currencies_to_usd:
                print('Invalid currency, try again')
            else:
                break

        while True:
            try:
                self.summ = float(input('Enter summ:\n'))
            except ValueError:
                print('Invalid summ, try again')
            else:
                if self.summ <= 0:
                    print('Invalid summ, try again')
                else:
                    break

        while True:
            self.target_currency = input('Enter target currency (EUR, UAH, RUR, GBP, USD):\n').upper()
            if self.target_currency not in self.currencies_to_usd:
                print('Invalid currency, try again')
            else:
                break


conv1 = Converter(currencies)
while True:
    if conv1.exit_flag:
        break
    conv1.input()
    conv1.calculate()
