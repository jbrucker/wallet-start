from typing import List
from cash import Cash
from money import Money


class Wallet:
    """An electronic wallet holds cash that you can insert and withdraw.
    """

    def __init__(self):
        """Create an empty wallet."""
        pass

    def deposit(self, *items):
        """Deposit cash into the wallet.

        :param items: one or more Cash items to deposit.
        :raises TypeError: if any of the items is not Cash.
        :raises ValueError: if any of the items has non-positive value.
        """
        pass

    def balance(self, currency: str) -> Money:
        """Return the balance of the wallet for a particular currency.

        It returns the total value of Money in the wallet having the
        requested currency (ignores any Money in other currencies).
        :param currency:  the currency to compute balance of
        :returns:  the total of Money in wallet having the requested currency.
        """
        pass
    
    def is_empty(self) -> bool:
        """Test if there is anything in the wallet."""
        pass

    def get_items(self) -> List[Money]:
        """Return a list of the items in the wallet.

        :returns: a copy of the list of items in the wallet.
        """
        pass
        
    def withdraw(self, amount: Money) -> List[Money]:
        """Withdraw cash from the wallet, so that the withdrawn amount
        has a value equal to amount, in the requested currency.

        :param amount: amount of Money to withdraw
        :returns: a list of cash items from the wallet whose total value
                equals the amount, and having the same currency as amount.
                Returns None if the withdraw cannot be performed.

        :raises ValueError: if amount.value is not positive
        :raises TypeError: if amount is not a Money object
        """
        #Hint: 
        #1. call a helper function to perform withdraw by recursion.
        #   the helper should not modify the list of items.
        #2. when the helper function returns, if it returned a list
        #   of cash to withdraw, then remove those items from the cash
        #   list of this wallet.  Then return the stuff you withdraw.

        towithdraw = withdraw_from(amount, self.items)



def withdraw_from(amount: Money, items: List[Money]) -> List[Money]:
    """Withdraw an amount from a list of Money (actually Cash) items.

    This is a helper method that decides what items (if any)
    should be withdrawn from the Wallet. It does not modify the parameters.

    :param amount: the amount of Money to withdraw
    :param items: a list of Cash items to choose from for withdraw. 
    :returns: a list of elements from the items parameter with value
              equal to amount. Returns None if cannot perform the withdraw.
    """
    # the algorithm is like the groupsum recursion problem.
    # but you can only withdraw items with currency matching
    # the currency in `amount`.
    pass
