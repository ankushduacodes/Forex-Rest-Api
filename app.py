import selenium
from flask import Flask, jsonify
from flask_restx import Api, Resource
from source import make_source_file
from scraper.forex_scraper import ForexScraper
from selenium.common.exceptions import TimeoutException

app = Flask(__name__)
api = Api(app)


@api.route('/api/forexInfo/')
class ForexInfo(Resource):
    def get(self):
        try:
            with open('euro.html', 'w+') as file:
                file.write(make_source_file())
        except NotADirectoryError:
            return jsonify({'Message': 'Please make sure you have chromedriver installed and the path to the driver is'
                                       ' correct'})
        except TimeoutException:
            return jsonify({'Message': 'Request timeout(Invensting.com servers took too much time to respond with '
                                       'requested information)'})
        except:
            jsonify({'Message': 'Something went wrong'})
        forex = ForexScraper()
        return jsonify(forex.get_info())


api.add_resource(ForexInfo, '/api/forexInfo/')

if __name__ == '__main__':
    app.run(port=3000)
