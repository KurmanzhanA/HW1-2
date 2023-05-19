class BankAccount:
class SavingAccount(BankAccount):
class CheckingAccount(BankAccount):

class Asset:
class BankAccount(Asset):
class RealEstate(Asset):
class Security(Asset):

class InterestBearingitem:
class BankAccount(InterestBearingitem):
class Security(InterestBearingitem):

class Insurableitem:
class BankAccount(Insurableitem):
class RealEstate(Insurableitem):

class Security:
class Stock(Security):
class Bond(Security):