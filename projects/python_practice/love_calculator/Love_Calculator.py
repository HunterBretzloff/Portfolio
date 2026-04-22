
def calculate_love_score(name1, name2):
    combined_string=(name1+name2).lower()
    t=combined_string.count("t")
    r=combined_string.count("r")
    u=combined_string.count("u")
    e=combined_string.count("e")

    l=combined_string.count("l")
    o=combined_string.count("o")
    v=combined_string.count("v")
    e=combined_string.count("e")

    true_score=t+r+u+e
    love_score=l+o+v+e

    total_score=int(str(true_score)+str(love_score))

    print(f"Your love score is {total_score}.")

calculate_love_score("Kanye West", "Kim Kardashian")