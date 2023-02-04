#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from manager_api import Business


# Open the business. NOTE: Always use a test business first!
business = Business("http://localhost:55667", "apiuser", "password", "Test Business")

# Retrieve the 10 most recent payments and display source account, payee, and total amount.
payments = business.Payment.list()[:10]
for pmt in payments:
    if pmt.Payee == "Customer":
        pmt_to = pmt.Customer.Name
    elif pmt.Payee == "Supplier":
        pmt_to = pmt.Supplier.Name
    else:
        pmt_to = pmt.Contact
    pmt_amt = sum([ln.Amount for ln in pmt.Lines])
    print(f"{pmt.Key} : {pmt_amt} : {pmt.PaidFrom.Name} -> {pmt_to}")

# Create a copy of the first payment with a line item doubled.
print("Creating new payment")
pmt = payments[0]
pmt.Key = None
pmt.Lines[0].Amount *= 2
pmt.Reference = "Test"
pmt.create()
pmt_amt = sum([ln.Amount for ln in pmt.Lines])
print(f"{pmt.Key} : {pmt_amt} : {pmt.PaidFrom.Name}")
input("Press Enter to continue...")

print("Updating the payment")
pmt.Reference = "Updated"
div = business.Division["Teaching"]
for ln in pmt.Lines:
    ln.Division = div
pmt.update()
input("Press Enter to continue...")

print("Deleting the payment")
pmt.delete()
