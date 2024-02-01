from database import get_current_tier


def get_difficulty():
    while True:
        print("Enter Difficulty Level: \n")
        print("For Easy - Type: Easy\nFor Medium -Type: Medium\nFor Hard - Type: Hard")
        level = input("Input Level: ").lower()
        if level in ("easy", "medium", "hard"):
            level = difficulty_level_verify(level)
            return level
        else:
            print("Enter Valid Answer...\n\n")


def difficulty_level_verify(level):
    highest_tier_E = 10
    highest_tier_M = 10
    current_level_tier = get_current_tier(level)

    if level != "hard":
        if current_level_tier in (highest_tier_E, highest_tier_M):
            print("Sorry, Highest Tier Reached!")
            get_difficulty()

    if level == "easy" and current_level_tier < highest_tier_E:
        return "easy"
    elif level == "medium" and current_level_tier < highest_tier_M:
        if get_current_tier("easy") >= 5:
            return "medium"
        else:
            print("You're not ready yet for medium levels. returning to easy..")
            return "easy"
    elif level == "hard":
        if get_current_tier("medium") >= 5:
            return "hard"
        elif get_current_tier("easy") >= 5:
            print("You're not ready yet for hard levels. returning to medium..")
            return "medium"
        else:
            print("You're not ready yet for hard or medium levels. returning to easy..")
            return "easy"
