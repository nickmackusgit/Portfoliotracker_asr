class PortfolioView:
    def show_menu(self):
        print("\n--- a.s.r. Portfolio Tracker ---")
        print("1. Asset toevoegen")
        print("2. Portfolio bekijken")
        print("3. Exit")
        return input("Kies een optie: ")

    def display_message(self, message):
        print(f"\n[INFO]: {message}")

    def show_weights(self, weights, title="Sector"):
        print(f"\n--- Verdeling per {title} ---")
        print(f"{title:<15} | {'Gewicht (%)':<10}")
        print("-" * 30)
        for category, weight in weights.items():
            print(f"{category:<15} | {weight:>10.2f}%")

    def show_portfolio(self, assets, total_value):
        print("\n--- Jouw Portfolio Overzicht ---")
        if not assets:
            print("Je portfolio is nog leeg.")
            return

        print(f"{'Ticker':<10} | {'Sector':<15} | {'Waarde':<10}")
        print("-" * 40)

        for asset in assets:
            waarde = asset.get_current_value()
            print(f"{asset.ticker:<10} | {asset.sector:<15} | €{waarde:>8.2f}")
        
        print("-" * 40)
        print(f"TOTALE PORTFOLIO WAARDE: €{total_value:,.2f}")

    def get_user_input(self, prompt):
        return input(f"{prompt}: ")