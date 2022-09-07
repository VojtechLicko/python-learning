import random


def flip_coin(number_of_flips):
    y = number_of_flips
    number_of_heads = 0
    number_of_tails = 0
    while y > 0:
        y -= 1
        seq = ["heads", "tails"]
        if random.choice(seq) == "heads":
            number_of_heads += 1
        else:
            number_of_tails += 1
    return f"Sample of {number_of_flips} \n\
{number_of_heads} heads were flipped, percentage:\
{(number_of_heads/number_of_flips)*100}\
\n {number_of_tails} tails were \
flipped percentage: {(number_of_tails/number_of_flips)*100}"


print(flip_coin(50000))
