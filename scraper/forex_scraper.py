from bs4 import BeautifulSoup


class ForexScraper:

    def __init__(self):
        self.source = open('./euro.html', 'r')
        self.info = {}

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
        print(row.find('td', class_=class_str).get_text())
        return row.find('td', class_=class_str).get_text()

    def get_timestamp(self, row, class_str):
        class_str = class_str.split()
        print(row.find('td', class_=class_str).get_text())
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

    def get_info(self):
        soup = BeautifulSoup(self.source, features='html5lib')
        tbody = soup.find('div', attrs={'id': 'cross_rates_container'}).find('tbody')

        usd_row = self.get_row(tbody, 'pair_1')
        usd_pid = 1
        euro_row = self.get_row(tbody, 'pair_2124')
        euro_pid = 2124
        jyp_row = self.get_row(tbody, 'pair_9')
        jyp_pid = 9
        gbp_row = self.get_row(tbody, 'pair_6')
        gbp_pid = 6
        aud_row = self.get_row(tbody, 'pair_15')
        aud_pid = 15
        cad_row = self.get_row(tbody, 'pair_16')
        cad_pid = 16
        chf_row = self.get_row(tbody, 'pair_10')
        chf_pid = 10
        sek_row = self.get_row(tbody, 'pair_61')
        sek_pid = 61
        nzd_row = self.get_row(tbody, 'pair_52')
        nzd_pid = 52
        inr_row = self.get_row(tbody, 'pair_1646')
        inr_pid = 1646

        self.info = {
            'EUR/USD': self.get_currency_info(usd_row, usd_pid),
            'USD/EUR': self.get_currency_info(euro_row, euro_pid),
            'EUR/JYP': self.get_currency_info(jyp_row, jyp_pid),
            'EUR/GBP': self.get_currency_info(gbp_row, gbp_pid),
            'EUR/AUD': self.get_currency_info(aud_row, aud_pid),
            'EUR/CAD': self.get_currency_info(cad_row, cad_pid),
            'EUR/CHF': self.get_currency_info(chf_row, chf_pid),
            'EUR/SEK': self.get_currency_info(sek_row, sek_pid),
            'EUR/NZD': self.get_currency_info(nzd_row, nzd_pid),
            'EUR/INR': self.get_currency_info(inr_row, inr_pid)
        }

        return self.info
