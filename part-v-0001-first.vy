# pragma version 0.4.0
# @license MIT

my_fav_proverb: public(String[50])

@deploy
def __init__():

    self.my_fav_proverb = "A rolling stone gathers no moss!"
