# -*- coding: utf-8 -*-

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

from pywhale.modules.decorators import validate_api_token_file

import os
import sys


class Utils (object):

    """
    Utility functions

    """

    def __init__(self):
        super(Utils, self)

    @staticmethod
    @validate_api_token_file
    def load_api_token(api_key_filepath):

        with open(api_key_filepath, 'rb') as f:
            key = f.readline().rstrip('\n')

        return key

    @staticmethod
    def get_welcome_msg():

        welcome_message = (
            "\n",
            "#" * 49,
            "\n",
            "#" * 6,
            "          Welcome to PyWhale         ",
            "#" * 6,
            "\n",
            "#" * 6,
            "   Python wrapper for whaleclub.co   ",
            "#" * 6,
            "\n",
            "#" * 49,
            "\n\n",
            "API token loaded, ready to trade!\n",
            "type PyWhale.help() at anytime to see available functions\n",
        )

        return ''.join(welcome_message)

    @staticmethod
    def help():
        """Returns a list of all callable functions"""

        help_message = """
        Available functions:
        -------------------

        General:
        --------
        get_markets()		Returns market information for one or more markets.
        get_price()		Returns the current bid and ask prices for one or more markets.
        get_balance()		Returns information about your balance.
        get_transactions()	List transactions that have occurred on your account.

        Live:
        -----
        create_position()	Submit a new position.
        get_position()		Fetch information about an existing position.
        update_position()	Fetch information about an existing position.
        close_position()        Close one active position at market price.
        cancel_position()	Cancel a pending position.
        split_position()        Split an existing pending or active position.
        list_positions()        List positions.

        Turbo:
        ------
        create_position()	Open a new turbo position.
        get_contracts()         Fetch a list of currently active turbo contracts.
        get_position()		Fetch information about an existing turbo position.
        list_positions()	List turbo positions.

        """

        print(help_message.r)
        return
