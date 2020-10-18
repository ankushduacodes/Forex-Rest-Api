# Forex-Rest-Api
# Description
Forex-Rest-Api is a simple Rest API which scraps the data from https://www.investing.com and sends it to the user whenever call to the API is made

# Requirements
- Python 3
- pip3
- compatible [chromedriver](https://chromedriver.chromium.org/downloads) (according to your operating system)

# Dependencies
To install all the dependencies of the project run the following command while in project directory
```bash
pip3 install -r requirements.txt
```

# Usage
1. Clone this repo or zip download it.
2. Install all the [dependencies](#dependencies)
3. Download compatible [chromedriver](https://chromedriver.chromium.org/downloads) (according to your operating system)
4. Copy the path where you have downloaded the chromedriver and run following command in the terminal or cmd:
    - For Windows:
        ```bash
        set path=<path to your chromedriver>
        ```
    - For macos and linux
         ```bash
        export path=<path to your chromedriver>
        ```
5. Open a terminal or cmd at downloaded or cloned folder directory.
```bash 
python3 app.py
```
6. This step will start a flask server at the localhost port 3000, Now go to http://localhost:3000/
7. Test the API using provided Swagger UI or make a postman GET request to http://127.0.0.1:3000/api/forexInfo/

# Output
Output is sent back in json format, may look something like:
```json
{
  "EUR/AUD": {
    "ask": "1.6557",
    "bid": "1.6547",
    "change": "+0.0058",
    "change_percent": "+0.35%",
    "high": "1.6586",
    "low": "1.6497",
    "timestamp": 1602881992,
    "title": "EUR/AUD - Euro Australian Dollar"
  },
  "EUR/CAD": {
    "ask": "1.5461",
    "bid": "1.5451",
    "change": "-0.0017",
    "change_percent": "-0.11%",
    "high": "1.5511",
    "low": "1.5437",
    "timestamp": 1602881996,
    "title": "EUR/CAD - Euro Canadian Dollar"
  },
  "EUR/CHF": {
    "ask": "1.0729",
    "bid": "1.0721",
    "change": "+0.0015",
    "change_percent": "+0.14%",
    "high": "1.0731",
    "low": "1.0699",
    "timestamp": 1602881993,
    "title": "EUR/CHF - Euro Swiss Franc"
  },
  "EUR/GBP": {
    "ask": "0.9075",
    "bid": "0.9070",
    "change": "+0.0010",
    "change_percent": "+0.12%",
    "high": "0.9110",
    "low": "0.9044",
    "timestamp": 1602881992,
    "title": "EUR/GBP - Euro British Pound"
  },
  "EUR/INR": {
    "ask": "86.0990",
    "bid": "86.0380",
    "change": "+0.1235",
    "change_percent": "+0.14%",
    "high": "86.1335",
    "low": "85.7720",
    "timestamp": 1602881992,
    "title": "EUR/INR - Euro Indian Rupee"
  },
  "EUR/JYP": {
    "ask": "123.55",
    "bid": "123.47",
    "change": "+0.08",
    "change_percent": "+0.06%",
    "high": "123.73",
    "low": "123.12",
    "timestamp": 1602881992,
    "title": "EUR/JPY - Euro Japanese Yen"
  },
  "EUR/NZD": {
    "ask": "1.7746",
    "bid": "1.7729",
    "change": "-0.0004",
    "change_percent": "-0.03%",
    "high": "1.7775",
    "low": "1.7716",
    "timestamp": 1602881995,
    "title": "EUR/NZD - Euro New Zealand Dollar"
  },
  "EUR/SEK": {
    "ask": "10.3779",
    "bid": "10.3598",
    "change": "-0.0184",
    "change_percent": "-0.18%",
    "high": "10.4087",
    "low": "10.3458",
    "timestamp": 1602881996,
    "title": "EUR/SEK - Euro Swedish Krona"
  },
  "EUR/USD": {
    "ask": "1.1721",
    "bid": "1.1717",
    "change": "+0.0013",
    "change_percent": "+0.11%",
    "high": "1.1746",
    "low": "1.1694",
    "timestamp": 1602881992,
    "title": "EUR/USD - Euro US Dollar"
  },
  "USD/EUR": {
    "ask": "0.8535",
    "bid": "0.8532",
    "change": "-0.0006",
    "change_percent": "-0.08%",
    "high": "0.8552",
    "low": "0.8514",
    "timestamp": 1602881992,
    "title": "USD/EUR - US Dollar Euro"
  }
}
```
## Future Imporvements
- [ ] Add JWT token authentication
