# pragma version 0.4.0
# @license MIT

salary_by_id: public(HashMap[uint8, uint32])

@deploy
def __init__():

    self.salary_by_id[24] = 62_000

    self.salary_by_id[101] = 74_500
