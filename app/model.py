import yfinance as yf

class Asset:
    def __init__(self, ticker, sector, asset_class, quantity, purchase_price):
        self.ticker = ticker
        self.sector = sector
        self.asset_class = asset_class
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.current_price = self.get_live_price()

    def get_live_price(self):
        data = yf.Ticker(self.ticker)
        price = data.history(period="1d")['Close'].iloc[-1]
        return price

    def get_current_value(self):
        return self.quantity * self.current_price

class PortfolioModel:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def calculate_total_value(self):
        total = 0
        for asset in self.assets:
            total += asset.quantity * asset.current_price
        return total

    def get_sector_weights(self):
        total_val = self.calculate_total_value()
        if total_val == 0:
            return {}

        sector_totals = {}
        for asset in self.assets:
            waarde = asset.quantity * asset.current_price
            sector = asset.sector
            sector_totals[sector] = sector_totals.get(sector, 0) + waarde

        weights = {}
        for sector, waarde in sector_totals.items():
            weights[sector] = (waarde / total_val) * 100
            
        return weights