import sqlite3
import uuid

# Function to create the SQLite3 database and tables
def create_database():
    conn = sqlite3.connect('invoice_system.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unique_id TEXT UNIQUE,
            name TEXT,
            email TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unique_id TEXT UNIQUE,
            customer_id INTEGER,
            date TEXT,
            total_amount REAL,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id INTEGER,
            description TEXT,
            quantity INTEGER,
            unit_price REAL,
            FOREIGN KEY(invoice_id) REFERENCES invoices(id)
        )
    ''')
    conn.commit()
    conn.close()

# Utility function to generate unique IDs
def generate_unique_id():
    return str(uuid.uuid4())

class InvoiceSystem:

    def __init__(self):
        self.conn = sqlite3.connect('invoice_system.db')
        self.cursor = self.conn.cursor()

    def create_customer(self, name, email):
        unique_id = generate_unique_id()
        self.cursor.execute('''
            INSERT INTO customers (unique_id, name, email)
            VALUES (?, ?, ?)
        ''', (unique_id, name, email))
        self.conn.commit()

    def create_invoice(self, customer_id, date, total_amount):
        unique_id = generate_unique_id()
        self.cursor.execute('''
            INSERT INTO invoices (unique_id, customer_id, date, total_amount)
            VALUES (?, ?, ?, ?)
        ''', (unique_id, customer_id, date, total_amount))
        self.conn.commit()

    def create_item(self, invoice_id, description, quantity, unit_price):
        self.cursor.execute('''
            INSERT INTO items (invoice_id, description, quantity, unit_price)
            VALUES (?, ?, ?, ?)
        ''', (invoice_id, description, quantity, unit_price))
        self.conn.commit()

    def update_invoice(self, invoice_id, date, total_amount):
        self.cursor.execute('''
            UPDATE invoices
            SET date = ?, total_amount = ?
            WHERE unique_id = ?
        ''', (date, total_amount, invoice_id))
        self.conn.commit()

    def delete_invoice(self, invoice_id):
        self.cursor.execute('''
            DELETE FROM items WHERE invoice_id IN (SELECT id FROM invoices WHERE unique_id = ?)
        ''', (invoice_id,))
        self.cursor.execute('''
            DELETE FROM invoices WHERE unique_id = ?
        ''', (invoice_id,))
        self.conn.commit()

    def retrieve_invoice(self, invoice_id):
        self.cursor.execute('''
            SELECT * FROM invoices WHERE unique_id = ?
        ''', (invoice_id,))
        invoice = self.cursor.fetchone()
        if invoice:
            self.cursor.execute('''
                SELECT * FROM items WHERE invoice_id = (SELECT id FROM invoices WHERE unique_id = ?)
            ''', (invoice_id,))
            items = self.cursor.fetchall()
            return {
                'invoice': invoice,
                'items': items
            }
        return None

    def list_customers(self):
        self.cursor.execute('''
            SELECT * FROM customers
        ''')
        customers = self.cursor.fetchall()
        return customers

    def list_invoices(self):
        self.cursor.execute('''
            SELECT invoices.unique_id, invoices.date, invoices.total_amount, customers.unique_id, customers.name
            FROM invoices
            JOIN customers ON invoices.customer_id = customers.id
        ''')
        invoices = self.cursor.fetchall()
        return invoices

    def list_invoices_for_customer(self, customer_id):
        self.cursor.execute('''
            SELECT invoices.unique_id, invoices.date, invoices.total_amount
            FROM invoices
            WHERE customer_id = ?
        ''', (customer_id,))
        invoices = self.cursor.fetchall()
        result = []
        for invoice in invoices:
            invoice_id = invoice[0]
            self.cursor.execute('''
                SELECT * FROM items WHERE invoice_id IN (SELECT id FROM invoices WHERE unique_id = ?)
            ''', (invoice_id,))
            items = self.cursor.fetchall()
            result.append({
                'invoice': invoice,
                'items': items
            })
        return result

    def close_connection(self):
        self.conn.close()

# Function to display the menu and handle user input
def main():
    create_database()

    while True:
        print("\nInvoice System")
        print("1. Create Customer")
        print("2. Create Invoice")
        print("3. Create Item")
        print("4. Update Invoice")
        print("5. Delete Invoice")
        print("6. Retrieve Invoice")
        print("7. List Customers")
        print("8. List Invoices")
        print("9. List Invoices for Customer")
        print("10. Exit")
        choice = input("Enter your choice: ")

        system = InvoiceSystem()

        if choice == '1':
            name = input("Enter Customer Name: ")
            email = input("Enter Customer Email: ")
            system.create_customer(name, email)
            print("Customer created successfully!")

        elif choice == '2':
            customer_id = input("Enter Customer ID: ")
            date = input("Enter Invoice Date (YYYY-MM-DD): ")
            total_amount = float(input("Enter Total Amount: "))
            system.create_invoice(customer_id, date, total_amount)
            print("Invoice created successfully!")

        elif choice == '3':
            invoice_id = input("Enter Invoice ID: ")
            description = input("Enter Item Description: ")
            quantity = int(input("Enter Quantity: "))
            unit_price = float(input("Enter Unit Price: "))
            system.create_item(invoice_id, description, quantity, unit_price)
            print("Item created successfully!")

        elif choice == '4':
            invoice_id = input("Enter Invoice ID to Update: ")
            date = input("Enter New Invoice Date (YYYY-MM-DD): ")
            total_amount = float(input("Enter New Total Amount: "))
            system.update_invoice(invoice_id, date, total_amount)
            print("Invoice updated successfully!")

        elif choice == '5':
            invoice_id = input("Enter Invoice ID to Delete: ")
            system.delete_invoice(invoice_id)
            print("Invoice deleted successfully!")

        elif choice == '6':
            invoice_id = input("Enter Invoice ID to Retrieve: ")
            result = system.retrieve_invoice(invoice_id)
            if result:
                print("Invoice Details:")
                print(f"ID: {result['invoice'][0]}")
                print(f"Customer ID: {result['invoice'][1]}")
                print(f"Date: {result['invoice'][2]}")
                print(f"Total Amount: {result['invoice'][3]}")
                print("\nItems:")
                for item in result['items']:
                    print(f"Description: {item[2]}, Quantity: {item[3]}, Unit Price: {item[4]}")
            else:
                print("Invoice not found!")

        elif choice == '7':
            customers = system.list_customers()
            print("All Customers:")
            for customer in customers:
                print(f"ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}")

        elif choice == '8':
            invoices = system.list_invoices()
            print("All Invoices:")
            for invoice in invoices:
                print(f"ID: {invoice[0]}, Date: {invoice[1]}, Total Amount: {invoice[2]}, Customer ID: {invoice[3]}, Customer Name: {invoice[4]}")

        elif choice == '9':
            customer_id = input("Enter Customer ID to List Invoices: ")
            invoices = system.list_invoices_for_customer(customer_id)
            print("Invoices for Customer:")
            for entry in invoices:
                print(f"\nInvoice ID: {entry['invoice'][0]}")
                print(f"Date: {entry['invoice'][1]}")
                print(f"Total Amount: {entry['invoice'][2]}")
                print("Items:")
                for item in entry['items']:
                    print(f"Description: {item[2]}, Quantity: {item[3]}, Unit Price: {item[4]}")
        
        elif choice == '10':
            print("Exiting the program...")
            system.close_connection()
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
