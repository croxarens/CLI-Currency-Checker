# CLI Currency Checker
A CLI tool to check and convert the currency values

A series of scripts for fetching info about the currencies.

## HOW TO INSTALL IT
You need to clone the code first. After that you can use the file money.py which is including the other files/scripts.

To make things easier, you can add the script inside CLI alias, so that you can run it without changing directory.


# HOW TO USE IT

`./money.py list`
Gives you a list of all the currencies.

`./money.py EUR GBP`
Gives you the value of 1 EUR in GBP.

`./money.py 34.5 EUR GBP`
Gives you the value of 34.5 EUR in USD

# Settings
There is a _settings.py_ file where you can setup your currency and the list of the other currencies you want to compare to.
So running just `./money.py` will read the info from the settings and give you the results.



# NOTE
 - The script has been tested on Linux, and it's using the /tmp/ forlder for caching some result.

Feel free to improve it.
