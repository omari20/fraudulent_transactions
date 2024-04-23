# from flask import Flask, request, jsonify, render_template
# import pandas as pd
# import psycopg2

# # Set up database connection parameters
# dbname = "E-Commerce_Transactions_db"
# user = "postgres"
# password = "postgres"
# host = "localhost"  # or the IP address of your database server
# port = "5432"       # default PostgreSQL port

# # Establish a connection to the database
# try:
#     connection = psycopg2.connect(
#         dbname=dbname,
#         user=user,
#         password=password,
#         host=host,
#         port=port
#     )
#     print("Database connection established.")

#      # Create a cursor object using the connection
#     cursor = connection.cursor()
    
#     # Execute a query
#     cursor.execute("SELECT version();")
#     db_version = cursor.fetchone()
#     print("PostgreSQL version:", db_version)
  
# except Exception as e:
#     print("An error occurred:", e)

# # Select all rows in the table
# cursor.execute("SELECT * FROM ecommerce_transactions;")

# # Fetch all rows from the result
# rows = cursor.fetchall()

# # Get column names
# column_names = [desc[0] for desc in cursor.description]


# # Create dataframe
# ecomm_transactions_df = pd.DataFrame(rows, columns=column_names)

# # Cleaning 1 (Addresses)
# ecomm_transactions_df['shipping_address'] = ecomm_transactions_df['shipping_address'].str.replace('\n', ', ')
# ecomm_transactions_df['billing_address'] = ecomm_transactions_df['billing_address'].str.replace('\n', ', ')

# # Clean 2 
# clean_transactn_df = ecomm_transactions_df.copy()

# clean_transactn_df['shipping_state'] = ecomm_transactions_df['shipping_address'].str.extract(r',\s*([A-Za-z]{2})\s*\d{5}')
# clean_transactn_df['billing_state'] = ecomm_transactions_df['billing_address'].str.extract(r',\s*([A-Za-z]{2})\s*\d{5}')



# app = Flask(__name__)

# @app.route('/dashboard')
# def dashboard(): 
#     return render_template('dashboard.html')

# def get_data():
    
#     # Filter data based on query parameters (e.g., payment method and product category)
#     payment_method = request.args.get('payment_method')
#     product_category = request.args.get('product_category')
    
#     filtered_data = clean_transactn_df
#     if payment_method:
#         filtered_data = filtered_data[filtered_data['payment_method'] == payment_method]
#     if product_category:
#         filtered_data = filtered_data[filtered_data['product_category'] == product_category]
    

#     # Convert DataFrame to dictionary
#     data_dict = clean_transactn_df.to_dict(orient='records')
    
#     # Convert dictionary to JSON using Flask's jsonify
#     return jsonify(data_dict)

# if __name__ == '__main__':
#     app.run(debug=True)


# connection.close()



from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import psycopg2





