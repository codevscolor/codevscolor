# https://codevscolor.com/python-bank-account-class
class Bank:
	def __init__(self):
		self.total_amount = 0
		self.name = ''

	def welcome(self):
		self.name = input('Welcome to your Bank Account. Please Enter your name: ')

	def print_current_balance(self):
		print('Your Current balance : {}'.format(self.total_amount))

	def deposit(self):
		self.total_amount += float(input('Hello {}, please enter amount to deposit: '.format(self.name)))
		self.print_current_balance()

	def withdraw(self):
		amount_to_withdraw = float(input('Enter amount to withdraw: '))

		if amount_to_withdraw > self.total_amount:
			print('Insufficient Balance !!')
		else:
			self.total_amount -= amount_to_withdraw

		self.print_current_balance()


if __name__=="__main__":
	bank = Bank()
	bank.welcome()

	while True:
		input_value = int(input('Enter 1 to see your balance,\n2 to deposit\n3 to withdraw\n'))

		if input_value == 1:
			bank.print_current_balance()
		elif input_value == 2:
			bank.deposit()
		elif input_value == 3:
			bank.withdraw()
		else:
			print('Please enter a valid input.')