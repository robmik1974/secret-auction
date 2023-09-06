from art import logo
import os


bid = list()


def add_new_bidder(name: str, bid_price: int) ->dict[str, int]:
    user_data = dict()
    user_data["name"] = name
    user_data["bid_price"] = bid_price
    return user_data
    

def find_the_highest_bidder(bid: dict[str, int]) ->tuple[str, int]:
    highest_bid = 0
    winner = ""
    for bidder in bid:
        if bidder["bid_price"] > highest_bid:
            highest_bid = bidder["bid_price"]
            winner = bidder["name"]
    
    return winner, highest_bid


def main():
    os.system('clear')
    should_continue = True
    while should_continue:
        print(logo)
        name = input("What is your name? ")
        bid_price = int(input("What is your bid price?: $"))
        bid.append(add_new_bidder(name=name, bid_price=bid_price))
        is_next_user = input("Are there other users who want to bid? 'yes' or 'no'?:\n")
        if is_next_user == 'no':
            should_continue = False
        else:
            os.system('clear')

    winner_name, winner_price = find_the_highest_bidder(bid)
    os.system('clear')
    print(logo)
    print(f"The winner is {winner_name} who paid ${winner_price}")


if __name__ == "__main__":
    main()
