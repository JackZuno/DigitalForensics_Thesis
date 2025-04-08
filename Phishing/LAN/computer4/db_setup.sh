# Inside the script
echo "Inside ds_setup Computer4"

# Wait 10 seconds
sleep 37

# Copy the content from a CSV file to a table
echo "First insert Computer4"
PGPASSWORD='james' psql -h database_server -d evil_corp -U jamesfoster -c "\COPY budget_info(section, detail, sub_detail) FROM './usr/local/files/budgetInformation.csv' DELIMITER ',' CSV HEADER;"

sleep 20

echo "Second insert Computer4"
PGPASSWORD='james' psql -h database_server -d evil_corp -U jamesfoster -c "\COPY contact_information(section, detail, sub_detail) FROM './usr/local/files/contactInformation.csv' DELIMITER ',' CSV HEADER;"

echo "End ds_setup Computer4"