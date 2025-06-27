import argparse
from db import init_db, add_expense, get_expenses

init_db()

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add")
add_parser.add_argument("date", help="Date (YYYY-MM-DD)")
add_parser.add_argument("category", help="Category")
add_parser.add_argument("description", help="Description")
add_parser.add_argument("amount", type=float, help="Amount")

view_parser = subparsers.add_parser("view")

args = parser.parse_args()

if args.command == "add":
    add_expense(args.date, args.category, args.description, args.amount)
    print("✅ Expense added successfully!")

elif args.command == "view":
    expenses = get_expenses()
    for e in expenses:
        print(f"{e[1]} | {e[2]} | {e[3]} | ₹{e[4]}")
else:
    parser.print_help()
