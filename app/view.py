class PortfolioView:
    def show_menu(self):
        print("\n--- a.s.r. Portfolio Tracker ---")
        print("1. Asset toevoegen")
        print("2. Portfolio bekijken")
        print("3. Exit")
        return input("Kies een optie: ")

    def display_message(self, message):
        print(f"\n[INFO]: {message}")