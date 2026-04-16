class Asset:
    def __init__(self, ticker, sector, asset_class, quantity, purchase_price):
        self.ticker = ticker
        self.sector = sector
        self.asset_class = asset_class
        self.quantity = quantity
        self.purchase_price = purchase_price

class PortfolioModel:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)