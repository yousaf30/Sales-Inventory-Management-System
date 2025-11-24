# Sales-Inventory-Management-System
A Python project for managing products, stock, sales, and reports — all stored using CSV files (Excel-friendly).

🚀 Features
➕ Add new products
📋 View product list
🛒 Sell items + auto stock update
🔄 Restock products
📉 Low stock alerts (≤ 5)
📊 Full sales report
🗑 Remove products

💾 Data saved in CSV (no database needed)
🛠️ Technologies Used
Python 3
CSV module
datetime module
CLI based menu

📂 Project Structure
inventory-system/
│── products.csv       # Auto-created
│── sales.csv          # Auto-created
│── main.py            # Project code
│── README.md

▶️ How to Run
1️⃣ Clone or download project
git clone https://github.com/yousaf30/Sales-Inventory-Management-System
2️⃣ Run the script
python main.py

3️⃣ Menu appears
1. Add Product
2. List Products
3. Sell Product
4. Restock Product
5. Sales Report
6. Low Stock Alert
7. Remove Product
0. Exit

📊 CSV Files Used
products.csv
sku,name,price,stock
P01,Keyboard,1200,10
P02,Mouse,600,5

sales.csv
date,sku,qty,total
2025-02-10 12:33:21,P01,2,2400

💡 Future Improvements
Add product search
Add category support
Export PDF reports
Add Tkinter GUI / Web version

👤 Author
Name: Your Name
GitHub:https://github.com/yousaf30/Sales-Inventory-Management-System
LinkedIn:www.linkedin.com/in/muhammad-yousaf-naz-a2583a395
