import csv

file_name = "homework_invoices.csv"

total_invoices = 0
high_amount_count = 0
invalid_amount_count = 0

try:
    with open(file_name, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for invoice in reader:

            total_invoices += 1

            # Read invoice details
            vendor = invoice["vendor"]
            amount = invoice["amount"]
            status = invoice["status"]

            print("\nInvoice Details")
            print("Vendor :", vendor)
            print("Amount :", amount)
            print("Status :", status)

            # Check amount
            try:
                if amount.strip() == "":
                    raise ValueError("Amount is missing")

                amount = float(amount)

                if amount > 100000:
                    high_amount_count += 1
                    print("Result : Amount is greater than 100,000")
                else:
                    print("Result : Amount is within the limit")

            except (ValueError, TypeError):
                invalid_amount_count += 1
                print("Result : Missing or invalid amount")

except FileNotFoundError:
    print("Error: CSV file was not found.")


# Final summary
print("\n========== SUMMARY ==========")
print("Total invoices read:", total_invoices)
print("Invoices greater than 100,000:", high_amount_count)
print("Invoices with missing/invalid amount:", invalid_amount_count)

