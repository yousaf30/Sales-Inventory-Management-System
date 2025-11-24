import csv
from datetime import datetime

PRODUCT_FILE = "products.csv"
SALES_FILE = "sales.csv"

def setup_files():
    try:
        with open(PRODUCT_FILE, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["sku", "name", "price", "stock"])
    except:
        pass

    try:
        with open(SALES_FILE, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "sku", "qty", "total"])
    except:
        pass

def load_products():
    setup_files()
    products = []
    with open(PRODUCT_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "sku": row["sku"],
                "name": row["name"],
                "price": float(row["price"]),
                "stock": int(row["stock"])
            })
    return products

def save_products(products):
    with open(PRODUCT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sku", "name", "price", "stock"])
        for p in products:
            writer.writerow([p["sku"], p["name"], p["price"], p["stock"]])

def add_product():
    products = load_products()

    sku = input("Enter SKU: ")

    for p in products:
        if p["sku"] == sku:
            print("This SKU already exists!")
            return

    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    products.append({"sku": sku, "name": name, "price": price, "stock": stock})
    save_products(products)

    print("Product added successfully!")

def list_products():
    products = load_products()

    if not products:
        print("No products available.")
        return

    print("\nSKU     Name                Price     Stock")
    print("-----------------------------------------------")
    for p in products:
        print(f"{p['sku']:7} {p['name']:15} {p['price']:8} {p['stock']}")

def sell_product():
    products = load_products()
    sku = input("Enter SKU to sell: ")

    for p in products:
        if p["sku"] == sku:
            qty = int(input("Quantity: "))

            if qty > p["stock"]:
                print("Not enough stock!")
                return

            p["stock"] -= qty
            save_products(products)

            total = qty * p["price"]

            with open(SALES_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), sku, qty, total])

            print(f"Sold! Total = {total}")
            return

    print("SKU not found!")


def restock():
    products = load_products()
    sku = input("Enter SKU to restock: ")

    for p in products:
        if p["sku"] == sku:
            qty = int(input("Quantity to add: "))
            p["stock"] += qty
            save_products(products)
            print("Restocked successfully!")
            return

    print("SKU not found!")

def sales_report():
    setup_files()
    total_sales = 0
    total_items = 0

    with open(SALES_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_sales += float(row["total"])
            total_items += int(row["qty"])

    print("\n--- Sales Report ---")
    print(f"Total Items Sold: {total_items}")
    print(f"Total Sales Amount: {total_sales}")

def low_stock():
    products = load_products()
    print("\nLow Stock Items (≤ 5):")

    found = False
    for p in products:
        if p["stock"] <= 5:
            print(f"{p['sku']} - {p['name']} (Stock: {p['stock']})")
            found = True

    if not found:
        print("No low stock items.")

def remove_product():
    products = load_products()
    sku = input("Enter SKU to remove: ")

    new_list = [p for p in products if p["sku"] != sku]

    if len(new_list) == len(products):
        print("SKU not found.")
    else:
        save_products(new_list)
        print("Product removed!")


def menu():
    setup_files()

    while True:
        print("\n--- SALES & INVENTORY SYSTEM (CSV) ---")
        print("1. Add Product")
        print("2. List Products")
        print("3. Sell Product")
        print("4. Restock Product")
        print("5. Sales Report")
        print("6. Low Stock Alert")
        print("7. Remove Product")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1": add_product()
        elif choice == "2": list_products()
        elif choice == "3": sell_product()
        elif choice == "4": restock()
        elif choice == "5": sales_report()
        elif choice == "6": low_stock()
        elif choice == "7": remove_product()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


# ------------------------------------------------------
if __name__ == "__main__":
    menu()
