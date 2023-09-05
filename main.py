from art import logo
import os


user_info = list()


def update_user_info(name: str, bid_price: int) ->None:
    user_data = dict()
    user_data["name"] = name
    user_data["bid_price"] = bid_price
    user_info.append(user_data)
    
    
def main():
    os.system('clear')
    should_continue = True
    while should_continue:
        print(logo)
        name = input("What is your name? ")
        bid_price = int(input("What is your bid price? $"))
        update_user_info(name=name, bid_price=bid_price)
        is_next_user = input("Are there other users who want to bid? 'yes' or 'no'? ")
        if is_next_user == 'no':
            should_continue = False
        else:
            os.system('clear')

    print(user_info)


if __name__ == "__main__":
    main()
