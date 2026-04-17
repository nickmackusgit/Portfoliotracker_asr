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
                new_asset = Asset("AAPL", "Tech", "Equity", 10, 150.0)
                self.model.add_asset(new_asset)
                self.view.display_message("Asset toegevoegd!")

            elif choice == '2':
                # Haal data uit het model
                assets = self.model.assets
                total_val = self.model.calculate_total_value()
                weights = self.model.get_sector_weights()
                
                # Toon het portfolio overzicht
                self.view.show_portfolio(assets, total_val)
                # Toon de sectorverdeling
                self.view.show_weights(weights, "Sector")

            elif choice == '3':
                break