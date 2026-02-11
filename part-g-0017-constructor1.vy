# pragma version ^0.4.0

founder: public(String[50])

last_time: public(uint256)

ended: public(uint256)

owner: public(address)


@deploy
def __init__(f: String[50], extra_time: uint256):

    self.founder = f 

    self.last_time = block.timestamp + extra_time 

    self.ended = block.timestamp

    self.owner = msg.sender

