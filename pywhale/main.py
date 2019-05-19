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

import os
from pywhale.modules.utils import Utils
from pywhale.modules.trade import General
# from pywhale.modules.trade import Live
# from pywhale.modules.trade import Turbo


class PyWhale(General):
    """Whaleclub.co cryptocurrency Exchange API Pyhon Client"""

    def __init__(self):

        # inherit token from API class for our connection class instance
        super(PyWhale, self).__init__()

        # api token keys
        self.default_key = 'BTC_demo_key'

        # Set to False if you don't wan't to see
        self.verbose = True

        # config
        self._api_keys_foldername = "api_keys"
        self._api_keys_filenames = [
            "BTC_demo_key.txt",
            "BTC_real_key.txt",
            "DASH_demo_key.txt",
            "DASH_real_key.txt",
            "ETH_real_key.txt",
            "LTC_real_key.txt"
        ]

        # get utility functions
        self._utils = Utils()
        self._init()

    def _init(self):

        self._load_api_token_files()
        print (self._utils.get_welcome_msg())
        print (self.help())


    def _load_api_token_files(self):
        """
        Store API token from the following files :

        BTC_demo_key.txt,
        BTC_real_key.txt,
        DASH_demo_key.txt,
        DASH_real_key.txt,
        ETH_real_key.txt,
        LTC_real_key.txt

        """
        def oj(a, b):
            return os.path.join(a, b)

        api_keys_folderpath = oj(
            os.path.dirname(os.path.abspath(__file__)),
            self._api_keys_foldername
        )

        # Store in instance all api token
        for api_token_filename in self._api_keys_filenames:
            setattr(
                self,
                api_token_filename.rstrip('.txt'),
                self._utils.load_api_token(
                    oj(api_keys_folderpath, api_token_filename)
                )
            )

        return True

    def help(self):
        return self._utils.help()

    # def _checkResp(self, resp):
    #     """Check whenever an response return an error"""
    #     parsed = json.loads(resp.text)

    #     # every thing is ok
    #     if resp.status_code == 200 or resp.status_code == 201:
    #         if self.verbose:
    #             print(json.dumps(parsed, indent=4, sort_keys=True))
    #         return parsed

    #     # we have an error
    #     else:

    #         print('\nOOps, somethings went Wrong!\n')

    #         try:
    #             print(parsed['error']['name'])
    #             print(parsed['error']['message'])
    #         except:
    #             print(parsed)

    # def _testSymbols(self, symb):
    #     if symb != '' and len(symb.split(',')) > 5:
    #         print('Error, You can only request information for up to 5 elements at once. Lower your input number and retry\n')
    #         return False
    #     else:
    #         return True

    # def _updateKey(self, key):

    #     if key is None:
    #         key = self.default_key

    #     # test if key parameter value is an accepted input
    #     l = ['BTC_real_key', 'BTC_demo_key', 'DASH_real_key',
    #          'DASH_demo_key', 'ETH_real_key', 'LTC_real_key']
    #     if key in l:
    #         i = l.index(key)
    #         k = [self.BTC_real_key, self.BTC_demo_key, self.DASH_real_key,
    #              self.DASH_demo_key, self.ETH_real_key, self.LTC_real_key]
    #         key = k[i]
    #     else:
    #         print("\nError, enter an acctepted value for key parameter, could either be 'BTC_real_key', 'BTC_demo_key', 'LTC_real_key', 'ETH_real_key', 'DASH_real_key' or 'DASH_demo_key' \n")
    #         return (False, key)

    #     return (True, key)
