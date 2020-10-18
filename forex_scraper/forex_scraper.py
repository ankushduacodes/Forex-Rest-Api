from bs4 import BeautifulSoup
from .fetch_html_source import fetch_html_source


class ForexScraper:
    """Scrapes the HTML source produced by fetch_html_source() function for the required info using beautiful soup
    """

    def __init__(self):
        self.source = fetch_html_source()

    def get_row(self, tbody, pair_id):
        """Scrapes required table row by its ID

        Args:
            tbody (bs4.element.tag): Table body from which we fetch the table rows
            pair_id (str): ID by which we fetch the desired table row

        Returns:
            bs4.element.tag: Returns desired table row by its ID
        """

        return tbody.find('tr', attrs={'id': pair_id})

    def get_title(self, row):
        """Scrapes title of the row

        Args:
            row (bs4.element.tag): Table row

        Returns:
            str: Return title of the row
        """

        class_str = 'bold left noWrap elp plusIconTd'.split()
        return row.find('td', class_=class_str).a.get('title')

    def get_bid(self, row, class_str):
        """Scrapes bid column of the desired row

        Args:
            row (bs4.element.tag): Table row
            class_str (str): class/classes based on which the bid data is scraped

        Returns:
            str: returns bid column value of the row
        """

        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_ask(self, row, class_str):
        """Scrapes ask column of the desired row

        Args:
            row (bs4.element.tag): Table row
            class_str (str): class/classes based on which the ask data is scraped

        Returns:
            str: returns ask column value of the row
        """

        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_high(self, row, class_str):
        """Scrapes high column of the desired row

        Args:
            row (bs4.element.tag): Table row
            class_str (str): class/classes based on which the high data is scraped

        Returns:
            str: returns high column value of the row
        """

        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_low(self, row, class_str):
        """Scrapes low column of the desired row

        Args:
            row (bs4.element.tag): Table row
            class_str (str): class/classes based on which the bid data is scraped

        Returns:
            str: returns low column value of the row
        """

        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_change(self, row, class_str):
        """Scrapes change column of the desired row

        Args:
            row (bs4.element.tag): Table row
            class_str (str): class/classes based on which the change data is scraped

        Returns:
            str: returns change column value of the row
        """

        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_change_percent(self, row, class_str):
        """Scrapes change percentage column of the desired row

        Args:
            row (bs4.element.tag): Table row
            class_str (str): class/classes based on which the change percentage data is scraped

        Returns:
            str: returns change percentage column value of the row
        """

        class_str = class_str.split()
        return row.find('td', class_=class_str).get_text()

    def get_timestamp(self, row, class_str):
        """Scrapes time column of the desired row

        Args:
            row (bs4.element.tag): Table row
            class_str (str): class/classes based on which the time data is scraped

        Returns:
            str: returns timestamp  of the row
        """

        class_str = class_str.split()
        return row.find('td', class_=class_str).get('data-value')

    def get_currency_info(self, row, pid):
        """Returns dictionary consisting of title, bid, high, low, change, change_percent and timestamp of a Table row which is identified by pid

        Args:
            row (bs4.element.tag): Table row
            pid (int): Pair ID of the column to be scraped

        Returns:
            dict: dictionary consisting of information about a row identified by its pid
        """
        # pid is injected into the class names using f strings to make it a multi-purpose function
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
        """Loops through the infomation inside of the list and calls get_currency_info to collect the infomation about all the diffent currencies into a dictionary.

        Args:
            currency_data_tuple_list (list of tuples): List of tuples constisting of key name and pair_IDs of the desired rows.
            tbody (bs4.element.tag): Table body from which the infomation is scraped.

        Returns:
            dict: Returns dinctionary having all the desired currency information
        """
        info_dict = {}
        for currency_data_tuple in currency_data_tuple_list:
            row = self.get_row(tbody, pair_id=f'pair_{currency_data_tuple[1]}')
            info_dict.update(
                {currency_data_tuple[0]: self.get_currency_info(row, currency_data_tuple[1])})
        return info_dict

    def get_info(self):
        """Top level function that invokes and handles the output of other functions

        Returns:
            dict: Return dictionary of information requested
        """

        soup = BeautifulSoup(self.source, features='html5lib')
        tbody = soup.find(
            'div', attrs={'id': 'cross_rates_container'}).find('tbody')
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
