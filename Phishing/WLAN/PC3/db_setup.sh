# Inside the script
echo "Inside ds_setup PC3"

# Wait 10 seconds
sleep 30

echo "First insert PC3"
# Copy the content from a CSV file to a table
PGPASSWORD='anna' psql -h database_server -d evil_corp -U annamoore -c "\COPY key_measurements(section, detail, sub_detail) FROM './usr/local/files/keyMeasurements.csv' DELIMITER ',' CSV HEADER;"

sleep 12

echo "Second insert PC3"
PGPASSWORD='anna' psql -h database_server -d evil_corp -U annamoore -c "\COPY locations(section, detail, sub_detail) FROM './usr/local/files/locations.csv' DELIMITER ',' CSV HEADER;"

echo "End ds_setup PC3"