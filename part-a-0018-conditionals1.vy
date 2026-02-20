# pragma version ^0.4.0

@external
@pure
def check_voter(age: uint8) -> bool:

    if age < 18 or age > 85:

        return False

    return True
