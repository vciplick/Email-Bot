# Welcome to BookExchange! 

This is intended for use in the annual Ciplickas family book exchange (and to prevent me from rewriting it from scratch for the third year in a row). 


# Running Instructions
## Inputs
The script takes in a argument `--file` that is a CSV of names and emails of people to  be included in the exchange. Example file: 

```
Santa Clause, reindeerwrangler@gmail.com
Mrs. Clause, cookietime@aol.com
Rudolph, rednose@yahoo.com
```
## Setup
This script requires access to a gmail account. I have set it up so you simply need to create a passwords config locally. Example file is located in passwords-EXAMPLE.confg; simply create a local `passwords.config` that contains your actual information. I highly reccomend using an App password instead of your ususal acount passowrd. 

## Executing 
As of now, I haven't created a proper setup, so simply run `python3 books.py -f <filename>`
