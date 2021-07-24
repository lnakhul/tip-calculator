import math

tip = (18, 20, 25)  # tuple to store tip amount


def totalTip():
    while True:
        try:
            user_input = input('What is your bill amount? \n')
            total_check = float(user_input)
            break
        except ValueError:
            print('Please enter a valid amount in number form.')

    while True:
        global total_tip
        for i in tip:
            total_tip = math.ceil(((i / 100) * total_check))  # Tip round up
            final_total = total_tip + total_check
            print(
                f'{i}% tip is ${total_tip}, which brings your total to ${final_total}')
        break


# Evenly split the tip and cost amoung each person
def splitTip():
    print('Calculating the total tip for each person')
    print('What is the size of your party?')
    total_party = int(input())
    while True:
        for i in tip:
            equal_tip = total_tip / total_party
            print(f'For {i}% tip, the individual amount is {equal_tip}')
        break


totalTip()
splitTip()
