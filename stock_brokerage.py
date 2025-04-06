import random

class Stock:
    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price

    def update_price(self):
        # Randomly update stock price (simulate market)
        change = random.uniform(-0.05, 0.05)
        self.price = round(self.price * (1 + change), 2)


class User:
    def __init__(self, username, balance=10000):
        self.username = username
        self.balance = balance
        self.portfolio = {}

    def buy_stock(self, stock, quantity):
        cost = stock.price * quantity
        if cost > self.balance:
            print(f"❌ Not enough balance to buy {quantity} shares of {stock.symbol}")
        else:
            self.balance -= cost
            self.portfolio[stock.symbol] = self.portfolio.get(stock.symbol, 0) + quantity
            print(f"✅ Bought {quantity} shares of {stock.symbol} at ₹{stock.price} each.")

    def sell_stock(self, stock, quantity):
        if self.portfolio.get(stock.symbol, 0) < quantity:
            print(f"❌ Not enough shares to sell.")
        else:
            self.portfolio[stock.symbol] -= quantity
            self.balance += stock.price * quantity
            print(f"✅ Sold {quantity} shares of {stock.symbol} at ₹{stock.price} each.")

    def view_portfolio(self, stocks):
        print(f"\n📊 {self.username}'s Portfolio:")
        for symbol, quantity in self.portfolio.items():
            if quantity > 0:
                stock = stocks[symbol]
                print(f"{symbol} - {quantity} shares @ ₹{stock.price}")
        print(f"💰 Balance: ₹{round(self.balance, 2)}\n")


class BrokerageSystem:
    def __init__(self):
        self.users = {}
        self.stocks = {
            "TCS": Stock("TCS", "Tata Consultancy Services", 3500),
            "INFY": Stock("INFY", "Infosys", 1400),
            "RELIANCE": Stock("RELIANCE", "Reliance Industries", 2600),
            "HDFC": Stock("HDFC", "HDFC Bank", 1650)
        }

    def create_user(self, username):
        if username in self.users:
            print("⚠️ User already exists.")
        else:
            self.users[username] = User(username)
            print(f"👤 User '{username}' created with ₹10,000 balance.")

    def get_user(self, username):
        return self.users.get(username)

    def update_stock_prices(self):
        for stock in self.stocks.values():
            stock.update_price()


# ---------------------------
# 🎮 CLI Simulation
# ---------------------------
def main():
    system = BrokerageSystem()

    while True:
        print("\n===== Online Stock Brokerage System =====")
        print("1. Create User")
        print("2. Buy Stock")
        print("3. Sell Stock")
        print("4. View Portfolio")
        print("5. Update Stock Prices")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            system.create_user(username)

        elif choice == "2":
            username = input("Enter username: ")
            user = system.get_user(username)
            if not user:
                print("❌ User not found.")
                continue
            symbol = input("Enter stock symbol (TCS, INFY, RELIANCE, HDFC): ").upper()
            quantity = int(input("Enter quantity: "))
            stock = system.stocks.get(symbol)
            if stock:
                user.buy_stock(stock, quantity)
            else:
                print("❌ Invalid stock symbol.")

        elif choice == "3":
            username = input("Enter username: ")
            user = system.get_user(username)
            if not user:
                print("❌ User not found.")
                continue
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            stock = system.stocks.get(symbol)
            if stock:
                user.sell_stock(stock, quantity)
            else:
                print("❌ Invalid stock symbol.")

        elif choice == "4":
            username = input("Enter username: ")
            user = system.get_user(username)
            if user:
                user.view_portfolio(system.stocks)
            else:
                print("❌ User not found.")

        elif choice == "5":
            system.update_stock_prices()
            print("📈 Stock prices updated!")

        elif choice == "6":
            print("👋 Exiting system. Goodbye!")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
