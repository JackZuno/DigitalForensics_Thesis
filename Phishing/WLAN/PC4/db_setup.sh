# Inside the script
echo "Inside ds_setup PC4"

# Wait 10 seconds
sleep 33

echo "First insert PC4"
# Copy the content from a CSV file to a table
PGPASSWORD='olivia' psql -h database_server -d evil_corp -U oliviamurphy -c "\COPY project_info(section, detail, sub_detail) FROM './usr/local/files/projectOverview.csv' DELIMITER ',' CSV HEADER;"

sleep 15

echo "Second insert PC4"
PGPASSWORD='olivia' psql -h database_server -d evil_corp -U oliviamurphy -c "\COPY team_involved(section, detail, sub_detail) FROM './usr/local/files/teamInvolved.csv' DELIMITER ',' CSV HEADER;"

echo "End ds_setup PC4"