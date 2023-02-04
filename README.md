# Python Manager API

This is a Python module to access the API provided by Manager accounting
software.

## WARNING

Use at your own risk! Always test API usage on a test business first!
Not responsible for any data loss or other problems (see license).

## Description

There is no official API documentation, but the API is meant to be self
documenting by browsing `/api` on a Manager server.

This module design is meant to automate much of the work, eliminate the
need to worry about GUID, and perform basic type checking and validation.

## Installation

`pip install manager_api`

## Configuration

To open a business, you need the server URL, username, password, and the
business name. It is recommended to create a separate user with suitable
permissions for the API access.

If using the local (personal) edition, first use the trial copy of the
server edition to create a user, then use http://localhost:55667 as the
server URL.

## Example Usage

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from manager_api import Business


# Open the business. NOTE: Always use a test business first!
business = Business("http://localhost:55667", "apiuser", "password", "Test Business")

# Retrieve the 10 most recent payments and display source account, payee, and total amount.
payments = business.Payment.list()[:10]
for p in payments:
    p.read()
    p.PaidFrom.read()
    if p.Payee == "Customer":
        p.Customer.read()
        p_to = p.Customer.Name
    elif p.Payee == "Supplier":
        p.Supplier.read()
        p_to = p.Supplier.Name
    else:
        p_to = p.Contact
    p_amt = sum([l.Amount for l in p.Lines])
    print(f"{p.Key} : {p_amt} : {p.PaidFrom.Name} -> {p_to}")

# Create a copy of the first payment with a line item doubled.
print("Creating new payment")
p = payments[0]
p.Key = None
p.Lines[0].Amount *= 2
p.Reference = "Test"
p.create()
p_amt = sum([l.Amount for l in p.Lines])
print(f"{p.Key} : {p_amt} : {p.PaidFrom.Name} -> {p_to}")

print("Updating the payment")
p.Reference = "Updated"
p.update()

print("Deleting the payment")
p.delete()
```
