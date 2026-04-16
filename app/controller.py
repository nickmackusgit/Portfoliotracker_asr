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
            elif choice == '3':
                break