class ClothesAgent:
    def __init__(self):
        self.weather = None

    def get_weather(self):
        # Simulating weather conditions (you can modify this as needed)
        self.weather = input("Enter the weather (sunny, rainy, windy, snowy): ").lower()

    def suggest_clothes(self):
        if self.weather == "sunny":
            print(
                "It's sunny outside. You should wear light clothes, sunglasses, and sunscreen."
            )
        elif self.weather == "rainy":
            print(
                "It's rainy outside. Don't forget an umbrella, raincoat, and waterproof shoes."
            )
        elif self.weather == "windy":
            print("It's windy outside. Wear layers and a jacket to stay warm.")
        elif self.weather == "snowy":
            print(
                "It's snowy outside. Dress warmly with a heavy coat, gloves, and boots."
            )
        else:
            print(
                "Sorry, I don't understand the weather condition. Please enter sunny, rainy, windy, or snowy."
            )


def main():
    agent = ClothesAgent()
    agent.get_weather()
    agent.suggest_clothes()


if __name__ == "__main__":
    main()
