import requests
import time

class ArbitrageBot:
    def __init__(self, exchange1_api_url, exchange2_api_url):
        self.exchange1_api_url = exchange1_api_url
        self.exchange2_api_url = exchange2_api_url

    def fetch_price(self, exchange_api_url):
        response = requests.get(exchange_api_url)
        data = response.json()
        return float(data["price"])

    def execute_trade(self, exchange_api_url, trade_data):
        response = requests.post(exchange_api_url, json=trade_data)
        return response.json()

    def find_arbitrage_opportunity(self):
        price1 = self.fetch_price(self.exchange1_api_url)
        price2 = self.fetch_price(self.exchange2_api_url)

        # Calculate potential profit percentage
        profit_percentage = (price2 - price1) / price1 * 100

        if profit_percentage > 0:
            # Perform arbitrage trade
            trade_data = {
                # Define trade parameters for buying on exchange 1 and selling on exchange 2
            }
            trade_result = self.execute_trade(self.exchange1_api_url, trade_data)
            print("Arbitrage opportunity found:")
            print(f"Buy on Exchange 1, Sell on Exchange 2")
            print(f"Profit Percentage: {profit_percentage}%")
            print(f"Trade Result: {trade_result}")
        else:
            print("No arbitrage opportunity found.")

    def run(self, interval_seconds):
        while True:
            self.find_arbitrage_opportunity()
            time.sleep(interval_seconds)

# Example usage
if __name__ == "__main__":
    exchange1_api_url = "https://exchange1.com/api"
    exchange2_api_url = "https://exchange2.com/api"

    bot = ArbitrageBot(exchange1_api_url, exchange2_api_url)
    bot.run(interval_seconds=10)
