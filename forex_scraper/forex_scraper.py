from bs4 import BeautifulSoup


class ForexScraper:

    def __init__(self):
        self.source = open('./euro.html', 'r')

    def get_row(self, tbody, pair):
        return tbody.find('tr', attrs={'id': pair})

    def get_title(self, row):
        class_str = 'bold left noWrap elp plusIconTd'.split()
        return row.find('td', class_=class_str).a.get('title')

    def get_bid(self, row, class_str):
        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_ask(self, row, class_str):
        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_high(self, row, class_str):
        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_low(self, row, class_str):
        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_change(self, row, class_str):
        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_change_percent(self, row, class_str):
        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_timestamp(self, row, class_str):
        class_str = class_str.split()
        return row.find('td', class_=class_str).get('data-value')

    def get_currency_info(self, row, pid):
        return {
            'title': self.get_title(row),
            'bid': self.get_bid(row, f'pid-{pid}-bid'),
            'ask': self.get_ask(row, f'pid-{pid}-ask'),
            'high': self.get_high(row, f'pid-{pid}-high'),
            'low': self.get_low(row, f'pid-{pid}-low'),
            'change': self.get_change(row, f'pid-{pid}-pc'),
            'change_percent': self.get_change_percent(row, f'pid-{pid}-pcp'),
            'timestamp': int(self.get_timestamp(row, f'pid-{pid}-time'))
        }

    def get_currency_info_dict(self, currency_data_tuple_list, tbody):
        info_dict = {}
        for currency_data_tuple in currency_data_tuple_list:
            row = self.get_row(tbody, pair=f'pair_{currency_data_tuple[1]}')
            info_dict.update({currency_data_tuple[0]: self.get_currency_info(row, currency_data_tuple[1])})
        return info_dict

    def get_info(self):
        soup = BeautifulSoup(self.source, features='html5lib')
        tbody = soup.find('div', attrs={'id': 'cross_rates_container'}).find('tbody')
        required_currency_data_tuple_list = [
            ('EUR/USD', 1),
            ('USD/EUR', 2124),
            ('EUR/JYP', 9),
            ('EUR/GBP', 6),
            ('EUR/AUD', 15),
            ('EUR/CAD', 16),
            ('EUR/CHF', 10),
            ('EUR/SEK', 61),
            ('EUR/NZD', 52),
            ('EUR/INR', 1646)
        ]
        return self.get_currency_info_dict(required_currency_data_tuple_list, tbody)
