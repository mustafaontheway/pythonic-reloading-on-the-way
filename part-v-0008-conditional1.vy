# pragma version 0.4.0
# @license MIT

@external
@pure
def can_vote(age: uint8) -> String[20]:

    if (age >= 18):

        return "He/She can vote"

    else:

        return "He/She can't vote"
