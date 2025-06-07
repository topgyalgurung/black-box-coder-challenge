#!/usr/bin/env python3

import sys

def calculate_reimbursement(days, miles, receipts):
    # Hybrid logic: conservative for short/medium, generous for long/high-mileage
    if days >= 7 or miles >= 800:
        # Generous for long/high-mileage trips
        if days >= 14 and receipts < 1000:
            # Special case for long trips with low receipts
            base_amount = days * 60
            trip_length_multiplier = 1.0
        else:
            base_amount = days * 95
            trip_length_multiplier = 1.25 if days >= 7 else 1.15 if days >= 5 else 1.05
        if miles >= 1000:
            mileage_amount = miles * 0.45
        elif miles >= 800:
            mileage_amount = miles * 0.35
        else:
            mileage_amount = miles * 0.22
        receipt_multiplier = 0.20 if days >= 7 else 0.10
    else:
        # Conservative for short/medium trips
        base_amount = days * 70
        mileage_amount = miles * 0.22
        receipt_multiplier = 0.4
        trip_length_multiplier = 1.05 if days == 5 else 1.0
    receipt_amount = receipts * receipt_multiplier
    total = (base_amount + mileage_amount + receipt_amount) * trip_length_multiplier
    return round(total, 2)

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 calculate_reimbursement.py <days> <miles> <receipts>")
        sys.exit(1)
    try:
        days = int(sys.argv[1])
        miles = float(sys.argv[2])
        receipts = float(sys.argv[3])
        if days < 1 or miles < 0 or receipts < 0:
            print("Invalid input: days must be ≥ 1; miles and receipts must be ≥ 0")
            sys.exit(1)
        result = calculate_reimbursement(days, miles, receipts)
        print(f"{result:.2f}")
    except ValueError:
        print("Invalid input: days must be an integer; miles and receipts must be numbers")
        sys.exit(1)

if __name__ == "__main__":
    main() 