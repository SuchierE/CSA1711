def decision_tree(weather, temperature):
    if weather == "Sunny":
        if temperature == "Hot":
            return "Do not play cricket"
        else:
            return "Play cricket"

    elif weather == "Rainy":
        return "Do not play cricket"

    elif weather == "Cloudy":
        return "Play cricket"

    else:
        return "Invalid weather condition"


weather = input("Enter weather (Sunny/Rainy/Cloudy): ").capitalize()
temperature = input("Enter temperature (Hot/Cool): ").capitalize()

result = decision_tree(weather, temperature)

print("Decision Tree Prediction:", result)
