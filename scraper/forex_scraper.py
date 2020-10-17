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

    def get_info(self):
        soup = BeautifulSoup(self.source, features='html5lib')
        tbody = soup.find('div', attrs={'id': 'cross_rates_container'}).find('tbody')

        usd_row = self.get_row(tbody, 'pair_1')
        euro_row = self.get_row(tbody, 'pair_2124')
        jyp_row = self.get_row(tbody, 'pair_9')
        gbp_row = self.get_row(tbody, 'pair_6')
        aud_row = self.get_row(tbody, 'pair_15')
        cad_row = self.get_row(tbody, 'pair_16')
        chf_row = self.get_row(tbody, 'pair_10')
        sek_row = self.get_row(tbody, 'pair_61')
        nzd_row = self.get_row(tbody, 'pair_52')
        inr_row = self.get_row(tbody, 'pair_1646')

        self.info = {
            'EUR/USD': {
                'title': self.get_title(usd_row),
                'bid': self.get_bid(usd_row, 'pid-1-bid'),
                'ask': self.get_ask(usd_row, 'pid-1-ask'),
                'high': self.get_high(usd_row, 'pid-1-high'),
                'low': self.get_low(usd_row, 'pid-1-low'),
                'change': self.get_change(usd_row, 'pid-1-pc'),
                'change_percent': self.get_change_percent(usd_row, 'pid-1-pcp'),
                'timestamp': int(self.get_timestamp(usd_row, 'pid-1-time'))
            },
            'USD/EUR': {
                'title': self.get_title(euro_row),
                'bid': self.get_bid(euro_row, 'pid-2124-bid'),
                'ask': self.get_ask(euro_row, 'pid-2124-ask'),
                'high': self.get_high(euro_row, 'pid-2124-high'),
                'low': self.get_low(euro_row, 'pid-2124-low'),
                'change': self.get_change(euro_row, 'pid-2124-pc'),
                'change_percent': self.get_change_percent(euro_row, 'pid-2124-pcp'),
                'timestamp': int(self.get_timestamp(euro_row, 'pid-2124-time'))
            },
            'EUR/JYP': {
                'title': self.get_title(jyp_row),
                'bid': self.get_bid(jyp_row, 'pid-9-bid'),
                'ask': self.get_ask(jyp_row, 'pid-9-ask'),
                'high': self.get_high(jyp_row, 'pid-9-high'),
                'low': self.get_low(jyp_row, 'pid-9-low'),
                'change': self.get_change(jyp_row, 'pid-9-pc'),
                'change_percent': self.get_change_percent(jyp_row, 'pid-9-pcp'),
                'timestamp': int(self.get_timestamp(jyp_row, 'pid-9-time'))
            },
            'EUR/GBP': {
                'title': self.get_title(gbp_row),
                'bid': self.get_bid(gbp_row, 'pid-6-bid'),
                'ask': self.get_ask(gbp_row, 'pid-6-ask'),
                'high': self.get_high(gbp_row, 'pid-6-high'),
                'low': self.get_low(gbp_row, 'pid-6-low'),
                'change': self.get_change(gbp_row, 'pid-6-pc'),
                'change_percent': self.get_change_percent(gbp_row, 'pid-6-pcp'),
                'timestamp': int(self.get_timestamp(gbp_row, 'pid-6-time'))
            },
            'EUR/AUD': {
                'title': self.get_title(aud_row),
                'bid': self.get_bid(aud_row, 'pid-15-bid'),
                'ask': self.get_ask(aud_row, 'pid-15-ask'),
                'high': self.get_high(aud_row, 'pid-15-high'),
                'low': self.get_low(aud_row, 'pid-15-low'),
                'change': self.get_change(aud_row, 'pid-15-pc'),
                'change_percent': self.get_change_percent(aud_row, 'pid-15-pcp'),
                'timestamp': int(self.get_timestamp(aud_row, 'pid-15-time'))
            },
            'EUR/CAD': {
                'title': self.get_title(cad_row),
                'bid': self.get_bid(cad_row, 'pid-16-bid'),
                'ask': self.get_ask(cad_row, 'pid-16-ask'),
                'high': self.get_high(cad_row, 'pid-16-high'),
                'low': self.get_low(cad_row, 'pid-16-low'),
                'change': self.get_change(cad_row, 'pid-16-pc'),
                'change_percent': self.get_change_percent(cad_row, 'pid-16-pcp'),
                'timestamp': int(self.get_timestamp(cad_row, 'pid-16-time'))
            },
            'EUR/CHF': {
                'title': self.get_title(chf_row),
                'bid': self.get_bid(chf_row, 'pid-10-bid'),
                'ask': self.get_ask(chf_row, 'pid-10-ask'),
                'high': self.get_high(chf_row, 'pid-10-high'),
                'low': self.get_low(chf_row, 'pid-10-low'),
                'change': self.get_change(chf_row, 'pid-10-pc'),
                'change_percent': self.get_change_percent(chf_row, 'pid-10-pcp'),
                'timestamp': int(self.get_timestamp(chf_row, 'pid-10-time'))
            },
            'EUR/SEK': {
                'title': self.get_title(sek_row),
                'bid': self.get_bid(sek_row, 'pid-61-bid'),
                'ask': self.get_ask(sek_row, 'pid-61-ask'),
                'high': self.get_high(sek_row, 'pid-61-high'),
                'low': self.get_low(sek_row, 'pid-61-low'),
                'change': self.get_change(sek_row, 'pid-61-pc'),
                'change_percent': self.get_change_percent(sek_row, 'pid-61-pcp'),
                'timestamp': int(self.get_timestamp(sek_row, 'pid-61-time'))
            },
            'EUR/NZD': {
                'title': self.get_title(nzd_row),
                'bid': self.get_bid(nzd_row, 'pid-52-bid'),
                'ask': self.get_ask(nzd_row, 'pid-52-ask'),
                'high': self.get_high(nzd_row, 'pid-52-high'),
                'low': self.get_low(nzd_row, 'pid-52-low'),
                'change': self.get_change(nzd_row, 'pid-52-pc'),
                'change_percent': self.get_change_percent(nzd_row, 'pid-52-pcp'),
                'timestamp': int(self.get_timestamp(nzd_row, 'pid-52-time'))
            },
            'EUR/INR': {
                'title': self.get_title(inr_row),
                'bid': self.get_bid(inr_row, 'pid-1646-bid'),
                'ask': self.get_ask(inr_row, 'pid-1646-ask'),
                'high': self.get_high(inr_row, 'pid-1646-high'),
                'low': self.get_low(inr_row, 'pid-1646-low'),
                'change': self.get_change(inr_row, 'pid-1646-pc'),
                'change_percent': self.get_change_percent(inr_row, 'pid-1646-pcp'),
                'timestamp': int(self.get_timestamp(inr_row, 'pid-1646-time'))
            }
        }

        return self.info
