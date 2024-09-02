print("Hello")

import psycopg2

def connect():
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(
            # dbname="irfanolia",
            dbname="postgres",
            user="postgres",
            password="KarachI01!",
            host="localhost",
            port="3010"
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a query
        #cursor.execute("SELECT version();")
       # cursor.execute("SELECT * from customer;")
        cursor.execute("SELECT * from order_info;")

        # Fetch and print the result of the query
        db_version = cursor.fetchone()
        #print(f"PostgreSQL database version: {db_version}")
        #print(f"Customers: {db_version}")
        print(f"Customer Info: {db_version}")

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except Exception as error:
        print(f"Error connecting to PostgreSQL database: {error}")


if __name__ == "__main__":
    connect()