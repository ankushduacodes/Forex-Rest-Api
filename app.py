from flask import Flask, jsonify
from flask_restx import Api, Resource
from forex_scraper.fetch_html_source import fetch_html_source
from forex_scraper.forex_scraper import ForexScraper
from selenium.common.exceptions import TimeoutException

app = Flask(__name__)
api = Api(app, version='1.0.0', title='Forex Rest API', description='API that scrapes latest infomation from '
                                                                    'https://www.investing.com/currencies/single'
                                                                    '-currency-crosses about following '
                                                                    'currencies:\n1. EUR/USD\n2. USD/EUR\n3. '
                                                                    'EUR/JYP\n4. EUR/GBP\n5. EUR/AUD\n6. EUR/CAD\n7. '
                                                                    'EUR/CHF\n8. EUR/SEK\n9. EUR/NZD\n10. '
                                                                    'EUR/INR\n\nIt scrapes following information:\n- '
                                                                    'Title\n- Bid\n- Ask\n- High\n- Low\n- Change\n- '
                                                                    'Change Percent\n- Timestamp')

api = api.namespace()


@api.route('/api/forexInfo/')
class ForexInfo(Resource):
    def get(self):
        """Handles GET requests to the API

        Returns:
            JSON: Returns json response to the GET requests
        """

        try:
            forex = ForexScraper()
        except NotADirectoryError:
            return jsonify({'Message': 'Please make sure you have chromedriver installed and the path to the driver is'
                                       ' correct'})
        except TimeoutException:
            return jsonify({'Message': 'Request timeout (Invensting.com servers took too much time to respond with '
                                       'requested information)'})
        except:
            return jsonify({'Message': 'Something went wrong'})

        return jsonify(forex.get_info())


api.add_resource(ForexInfo, '/api/forexInfo/')

if __name__ == '__main__':
    app.run()
