from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

# Your database setup goes here

import sqlite3

# Create a new SQLite database
conn = sqlite3.connect('frontdeskapp.db')

# Create a table for storage customers
conn.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone_number TEXT NOT NULL
    )
''')

conn.commit()
conn.close()


# Your routes will be defined later

@app.route('/new-customer', methods=['GET'])
def new_customer_page():
    return render_template('new_customer.html')




@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        first_name = data['first_name']
        last_name = data['last_name']
        phone_number = data['phone_number']

        # Insert customer into the database
        conn = sqlite3.connect('frontdeskapp.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO customers (first_name, last_name, phone_number)
            VALUES (?, ?, ?)
        ''', (first_name, last_name, phone_number))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Customer created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400



@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:
        conn = sqlite3.connect('frontdeskapp.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
        customer = cursor.fetchone()
        conn.close()

        if customer is None:
            return jsonify({'message': 'Customer not found'}), 404

        customer_data = {
            'id': customer[0],
            'first_name': customer[1],
            'last_name': customer[2],
            'phone_number': customer[3]
        }

        return jsonify(customer_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400




if __name__ == '__main__':
    app.run(debug=True)

