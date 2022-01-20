from money import Money
import datetime


class Cash(Money):
    """Cash represents physical units of money, namely coins and banknotes."""

    def __init__(self, value, currency):
        """Initial a new cash object. The value must be positive."""
        #TODO verify the value is positive, then call superclass constructor
        pass
    

#TODO write the Coin and Banknote classes. They are subclasses of Cash.
class Coin:
    """Currency minted as coins, with a year."""
    pass 
    #TODO constructor calls superclass constructor
    #TODO constructor sets the _year attribute to this year
 

#fix this class
class Banknote:
    """Currency in the form of paper money, with a year.

       The value of a Banknote must be a multiple of 10 units of currency.
    """
    pass
