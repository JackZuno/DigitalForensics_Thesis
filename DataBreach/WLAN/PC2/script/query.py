import argparse
import psycopg2
import csv

# Database connection parameters
DB_HOST = 'database_server'  # Replace with your database server's IP address
DB_NAME = 'evil_corp'         # Replace with your database name
DB_USER = 'sarahwilliams'     # Replace with your username
DB_PASSWORD = 'sarah'         # Replace with your password

def fetch_data(table_name):
    try:
        # Connect to the database
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cursor = connection.cursor()

        # Execute a SQL query to fetch data from the table
        cursor.execute(f'SELECT * FROM {table_name};')

        # Retrieve all rows from the executed query
        records = cursor.fetchall()

        # Get column names from the cursor description
        column_names = [desc[0] for desc in cursor.description]

        return column_names, records

    except Exception as e:
        print(f"Error while fetching data: {e}")
        return None, None

    finally:
        if connection:
            cursor.close()
            connection.close()

def write_to_csv(table_name, column_names, records):
    """Write the retrieved data to a CSV file."""
    try:
        csv_file = f"./usr/local/files/{table_name}.csv"
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write the column names as the header
            writer.writerow(column_names)

            # Write the data rows
            for record in records:
                writer.writerow(record)

        print(f"Data successfully written to {csv_file}")

    except Exception as e:
        print(f"Error while writing to CSV: {e}")

def main(table_name):
    # Fetch data from the database
    column_names, records = fetch_data(table_name)

    # If data is fetched successfully, write it to CSV
    if records is not None:
        write_to_csv(table_name, column_names, records)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch data from PostgreSQL and write to CSV')
    parser.add_argument('TABLE_NAME', help='Name of the table to fetch data from')

    args = parser.parse_args()
    main(args.TABLE_NAME)
