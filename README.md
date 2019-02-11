# Rescale-Data-Pipeline

A simple data pipeline architecture that reads data from an S3 bucket and stores it in a MySQL DB.

***Technologies Used/Required***
1. Airflow - To orchestrate and schedule the pipeline. The scheduler runs everyday at 00:10hrs UTC everyday.
2. Python - To code the airflow pipeline logic and also pull the data from the S3 bucket and perform necessary transformation on it.
3. MySQL - Used as a DB to store the resultant data.
4. Virtualenv - Required to install & initialize airflow.
5. AWS EC2 - Used to host the application.

***Environment***
AWS EC2 Linux Amazon AMI of instance type t2.micro
Conda4.6.2 with python3.4+

***Usage***

The following are the required steps to start the pipeline for the environment mentioned above:

1. Initialize Airflow:

- 'cd' into the airflow home(where the airflow is installed and configured with $AIRFLOW_HOME
- Activate the virtualenv - Use the command 'source <path-to-virtualenv>/bin/activate'
- Start airflow webserver - Use the command 'airflow webserver'
- Start the airflow scheduler - Repeat steps i and ii and type 'airflow scheduler' 

2. In a web browser, type the following: \<public-IP-of-EC2>\:8080

***Output***

The code creates the following directories:

- data - Stores the data pulled from S3.
- added_data - Data that has been added to the MySQL table.
- logs - Stores the logs of the process.

***Note***

If any issues are being experienced by Airflow. Please run the scripts individually as following in the order specified:

1. Run the python script:

- python get_s3data.py 

2. Run the bash script:

- bash insert_to_sql.sh
 
