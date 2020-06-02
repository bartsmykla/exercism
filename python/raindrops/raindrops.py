def convert(number):
    drops = {
        105: "PlingPlangPlong",
        35: "PlangPlong",
        21: "PlingPlong",
        15: "PlingPlang",
        7: "Plong",
        5: "Plang",
        3: "Pling",
    }

    for divider, result in drops.items():
        if number % divider == 0:
            return result
    else:
        return str(number)
