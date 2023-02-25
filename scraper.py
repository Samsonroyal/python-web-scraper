import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='username', password='password',
                              host='database-host', database='database-name')

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Define the SQL query to insert data into the database
add_job = ("INSERT INTO jobs "
           "(title, company, location, link) "
           "VALUES (%s, %s, %s, %s)")

# Loop through the job listings and insert them into the database
for job in jobs:
    job_data = (job['title'], job['company'], job['location'], job['link'])
    cursor.execute(add_job, job_data)

# Commit the changes to the database
cnx.commit()

# Close the database connection
cursor.close()
cnx.close()