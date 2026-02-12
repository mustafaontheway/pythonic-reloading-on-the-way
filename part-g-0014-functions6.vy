# pragma version ^0.4.0

voter_ages: public(uint8[10])

index: public(uint8)

@external
def add_voter_age(age: uint8):

    if age > 90:

        raise "Voter age must be smaller than 90!"

    if self.index >= 10:

        raise "Voter list is full! (10 voters)"

    self.voter_ages[self.index] = age

    self.index += 1
