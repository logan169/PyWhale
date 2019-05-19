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

from functools import wraps
import sys
import json


def validate_api_token_file(func):
    """
    Validate that the returned API token from a file is legit

    """

    @wraps(func)
    def _validate(api_key_filepath):
        api_token = func(api_key_filepath)
        if len(api_token) != 36:
            err_msg = (
                "\nError, API token for {} is either missing or incomplet"
                " (length is not equal to 36 characters)\n"
                "Check that you've correctly enter "
                "your API token in {}"
            ).format(api_key_filepath, api_key_filepath)
            sys.exit(err_msg)
        return api_token

    return _validate


def validate_key_value(func):
    """
    Validate that API token value used is legit

    """

    keys_list = [
        'BTC_real_key', 'BTC_demo_key', 'DASH_real_key',
        'DASH_demo_key', 'ETH_real_key', 'LTC_real_key'
    ]

    @wraps(func)
    def _validate(self, key):

        if not key:
            key = self.default_key

        if key in keys_list:
            return getattr(self, keys_list.index(key))

        raise Exception(
            "An error occured: Api key: {} is not in {}".format(
                key,
                keys_list
            )
        )

        return None

    if _validate:
        return func


def validate_symbols(func):
    """
    Validate that markets passed as parameters are legit

    """

    @wraps(func)
    def _validate(symbols):

        symbols = symbols.split(',')
        if len(symbols) > 5:
            return False
        return True

    if not _validate:
        print ("An error occured: Markets symbols are not legit")
        return None

    return _validate


# # def validate_request_response(func):
# #     """
# #     Validate that the returned requests response is not None

# #     """

# #     @wraps(func)
# #     def _validate(raw_response):

# #         parsed_response = json.loads(resp.text)

# #         # response exists
# #         if raw_response.status_code in [200, 201]:
# #             return parsed_response

# #         print ("An error occured:\n")
# #         try:
# #             print(parsed_response['error']['name'])
# #             print(parsed_response['error']['message'])
# #         except:
# #             print(parsed_response)
# #         return None

# #     return _validate




# def verbosity_print(func):
#     """
#     Print returned data if verbosity parameter is set to True

#     """

#     @wraps(func)
#     def _evaluate_verbosity:

#         return None

#     return _evaluate_verbosity
