import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> list[int]:
    """"""
    a = []
    a.append(len(players.axes[0]))
    a.append(len(players.axes[1]))
    return a


players = pd.DataFrame(
    {
        "player_id ": [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
        "name": [
            "Mason",
            "Riley",
            "Bob",
            "Isabella",
            "Zachary",
            "Ava",
            "Violet",
            "Thomas",
            "Jack",
            "Charlie",
        ],
        "age": [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
        "position": [
            "Forward",
            "Winger",
            "Striker",
            "Goalkeeper",
            "Midfielder",
            "Defender",
            "Striker",
            "Striker",
            "Midfielder",
            "Center-back",
        ],
        "team": [
            "RealMadrid",
            "Barcelona",
            "ManchesterUnited",
            "Liverpool",
            "BayernMunich",
            "Chelsea",
            "Juventus",
            "ParisSaint-Germain",
            "ManchesterCity",
            "Arsenal",
        ],
    }
)

print(getDataframeSize(players))
