# Author: Logan Schwartz
# This file is part of pywhale.
# pywhale is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pywhale is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser
# General Public LICENSE along with krakenex. If not, see
# <http://www.gnu.org/licenses/gpl-3.0.txt>.

import requests
from statistics import mean


class General(object):
	"""	Whaleclub.co cryptocurrency Exchange API Pyhon Client general functions:"""

	def getMarkets(self, symbols='',key=None):
		"""
Returns market information for one or more markets.
Default returns a list of of available markets with basic information such as display name and category.

args:
-----
symbols 	string 		List of one or more comma-separated market symbols. You can request market information for up to 5 markets at once. Default is "" and return all symbols
key     	string 		One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
display_name	string	The market’s conventional name.
leverages 		array   Leverage levels available.
limits 			integer	Maximum active position size for each base currency
hours 			string	Market operating hours. Market is closed at all other times.
financing_rate 	number	Daily financing rate. Multiply by 100 to get the amount in percent.
category 		string	Asset class.
turbo 			object	Information about turbo trading, if it’s available for this market. The payoff object contains the contract duration (in minutes) and the associated payoff.

		"""

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#check symbols does not exceed 5 values
		if self._testSymbols(symbols) is False:
			return

		#Create request elements
		url = self.start_url+'markets/' + str(symbols)
		h = {"Authorization":"Bearer "+key}
		r = requests.get(url,headers=h)

		if self.verbose:
		    print('\nMarkets informations: \n')

		return self._checkResp(r)


	def _calcspread(self, price):
		"""Calculates absolute and perc. spread and adds it to the input object.
Accepts a price-object as returned from getPrice
		"""
		for key, value in price.items():
				diff = float(value["ask"]) - float(value["bid"])
				diffp = diff / \
				mean([float(value["ask"]), float(value["bid"])]) * 100
				if self.verbose:
						print("Market: ", key, "\tAbs:", diff, "\trel:", diffp)
				price[key]["diff_abs"] = diff
				price[key]["diff_perc"] = diffp

		return price


	def getPrice(self,symbols,key=None, spread=True):
		"""
Returns the current bid and ask prices for one or more markets.

args:
-----
symbols		string 		List of one or more comma-separated market symbols. You can request market information for up to 5 markets at once. Default is "" and return all symbols
key		string 		One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key
spread	boolean		Calculate spread and add that to the response object
resp:
-----
bid 		number		The current bid price.
ask 		number		The current ask price.
state 		string		Can be open, closed, pre (pre-market trading – stocks only), or after (after-market trading – stocks only)
last_updated	integer		When prices for this market were last updated.
diff_abs	number		Absolute Spread if requested
diff_perc	number		Percentage Spread if requested
		"""
		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#check symbols does not exceed 5 values
		if self._testSymbols(symbols) is False:
			return

		#check symbols is not 0
		if symbols == '':
			print ('Error, you should at least submit one element in the symbols parameter.\n')
			return

		#Create request elements
		url = self.start_url+'price/' + str(symbols)
		h = {"Authorization":"Bearer "+key}
		r = requests.get(url,headers=h)

		if self.verbose:
			print('\nPrice informations: \n')



		prices = self._checkResp(r)
		if not spread:
				return prices
		else:
				return self._calcspread(prices)


	def getBalance(self,key=None):
		"""
Returns information about your balance.
BTC/DASH real or demo balance information will be returned based on whether you pass 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key' as key parameter.

args:
-----
key     	string 		One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
available_amount	integer		Balance available to trade, in satoshis.
total_amount		integer		Total balance, in satoshis.
unconfirmed_amount	integer		Deposit amount that has not yet confirmed, in satoshis.
deposit_address		string		Your deposit address.
active_amount		object		Balance used in active positions across markets, in satoshis.
pending_amount		object		Balance used in pending positions across markets, in satoshis.
active_amount_turbo	object		Balance used in active turbo positions across markets, in satoshis.
last_updated		integer		When your balance was last updated.
currency		string		Base currency.
		"""

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'balance'
		h = {"Authorization":"Bearer "+key}
		r = requests.get(url,headers=h)

		if self.verbose:
			print ('\nYour balance informations: \n')

		return self._checkResp(r)

	def getTransactions(self, transaction_type='deposits',limit=5, key=None):
		"""
List transactions that have occurred on your account.
Use this function to request a list of transactions. transaction_type can be deposits, withdrawals, referrals, or bonuses. Defaults to deposits.
Transactions returned are sorted by creation date (created_at).

args:
-----
transaction_type	string		transaction_type can be 'deposits', 'withdrawals', 'referrals', or 'bonuses'. Defaults to deposits.
limit 			integer 	Optional. Number of results per request. Defaults to 5. Max is 50.
key     		string 		One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id 		string		Unique ID for the transaction.
amount 		integer 	Value of the transaction, in satoshis.
state 		string 		Can be pending or complete. Appears only for deposits and withdrawals.
hash 		string 		Bitcoin transaction hash. Appears only for deposits.
address 	string 		Destination Bitcoin address. Appears only for withdrawals.
created_at 	integer 	When the transaction was made.
currency 	string 		Base currency.
		"""

		#test limit parameter value
		if limit < 1 or limit > 50:
			print ('\nError, limit parameter value should be between 0 and 50')
			return

		#test transaction_type parameter value
		if transaction_type not in ['deposits','withdrawals','referrals','bonuses']:
			print ("\nError, transaction_type parameter value should be either 'deposits','withdrawals','referrals','bonuses'")
			return

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'transactions/'+transaction_type
		h = {"Authorization":"Bearer "+key}
		d = {'limit':limit}
		r = requests.get(url,headers=h,)

		if self.verbose:
			print ('\nYour Transactions history: \n')

		return self._checkResp(r)

	@classmethod
	def help(self,function_name = None):
		"""Returns a list of all callable functions"""
		help_message = """
Available functions:
-------------------

General:
--------
help()			Returns a list of all callable functions.
getMarkets()		Returns market information for one or more markets.
getPrice()		Returns the current bid and ask prices for one or more markets.
getSpread()		Returns the spread for a specified market
getBalance()		Returns information about your balance.
getTransactions()	List transactions that have occurred on your account.

Live:
-----
newPosition()		Submit a new position.
getPosition()		Fetch information about an existing position.
updatePosition()	Fetch information about an existing position.
closePosition()		Close one or multiple active positions at market price.
cancelPosition()	Cancel one or multiple pending positions.
splitPosition()		Split an existing pending or active position.
listPositions()		List positions.

Turbo:
------
getTurboActiveContracts()	Fetch a list of currently active turbo contracts.
createNewTurboPosition()	Open a new turbo position.
getTurboPosition()		Fetch information about an existing turbo position.
listturboPositions()		List turbo positions.

You could type print(PyWhale.function_name.__doc__) to get more info about any function
		"""

		print (help_message)
		return
