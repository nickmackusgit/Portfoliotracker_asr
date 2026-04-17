from app.model import PortfolioModel, Asset
from app.view import PortfolioView

class PortfolioController:
    def __init__(self):
        self.model = PortfolioModel()
        self.view = PortfolioView()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                ticker = self.view.get_user_input("Voer de ticker in (bijv. AAPL)")
                sector = self.view.get_user_input("Voer de sector in (bijv. Tech)")
                asset_class = self.view.get_user_input("Voer de asset class in (bijv. Equity)")
                
                quantity = float(self.view.get_user_input("Voer het aantal stuks in"))
                price = float(self.view.get_user_input("Voer de aankoopprijs in"))

                new_asset = Asset(ticker, sector, asset_class, quantity, price)
                self.model.add_asset(new_asset)
                
                self.view.display_message(f"Asset {ticker} succesvol toegevoegd!")

            elif choice == '2':
                assets = self.model.assets
                total_val = self.model.calculate_total_value()
                weights = self.model.get_sector_weights()
                
                self.view.show_portfolio(assets, total_val)
                # Toon de sectorverdeling
                self.view.show_weights(weights, "Sector")

            elif choice == '3':
                break