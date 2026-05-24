from accounts import create_account
from transaction import deposit, withdraw

create_account("ACC001", "Nimal", 1000)

deposit("ACC001", 500)

withdraw("ACC001", 200)