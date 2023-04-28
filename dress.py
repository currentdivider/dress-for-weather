from agents.weather_agent import weather_agent

if __name__ == "__main__":

    city = input("Enter city name:")
    print(weather_agent(city=city))