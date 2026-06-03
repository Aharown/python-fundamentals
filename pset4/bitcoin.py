import requests
import sys

# # Bitcoin is a form of digital currency, otherwise known as cryptocurrency.
# Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network,
# otherwise known as a blockchain, to record transactions.

# # Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one
# currency (e.g., USD) for Bitcoin.

# # In a file called bitcoin.py, implement a program that:

# # Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy.
# If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# # Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey.
# You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard,
# which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
# Be sure to catch any exceptions, as with code like:
# # import requests

# # try:
# #     ...
# # except requests.RequestException:
# #     ...
# # Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.

#pseudocode
# import requests
# import sys


# function for bitcoin amount
# try block
# check length of sys.argv
# if too short exit
# assign amount var sys.argv[1]
# if amount is not an integer,
# except ValueError("Wrong command, select amount")
# sys.exit
# return amount

# Time: O(1)
# Space: O(1) no growing DS, all fixed

def main():
    amount = bitcoin_amount()
    price = api_call()
    total = amount * price
    print(f"{total:,.4f}")

def bitcoin_amount():
    if len(sys.argv) < 2:
            sys.exit("Missing command-line argument")
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Wrong command, select amount")

# function for API call
# try block
# function receives amount var
# assign response var with api call
# except request error
# iterate over response and get the current price of bc as a float store in var
# multiply it by the received bitcoin var from sys.argv and return amount to 4 dec with , as a sep

def api_call():
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=f69010d483a4deb9fe5b0faf9a63a39bca4411a04b139d64fcc0852095aa7f77")
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Could not get Bitcoin price")


if __name__ == "__main__":
    main()
