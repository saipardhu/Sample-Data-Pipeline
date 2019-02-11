# Rescale-Data-Pipeline

A simple data pipeline architecture that reads data from an S3 bucket and stores it in a MySQL DB.

***Technologies Used***
1. Airflow - To orchestrate and schedule the pipeline.
2. Python - To code the airflow pipeline logic and also pull the data from the S3 bucket and perform necessary transformation on it.
3. MySQL - Used as a DB to store the resultant data.
4. Virtualenv - Required to install & initialize airflow.
5. AWS EC2 - Used to host the application.

***Environment***
AWS EC2 Amazon AMI of instance type t2.micro

***Usage***

The following are the required steps to start the pipeline for the environment mentioned above:

1. Initialize Airflow:

    i.'cd' to the airflow home(where the airflow is installed and configured with $AIRFLOW_HOME
    ii.Activate the virtualenv - Use the command 'source <path-to-virtualenv>/bin/activate'
    iii.Start airflow webserver - Use the command 'airflow webserver'
    iv.Start the airflow scheduler - Repeat steps i and ii and type 'airflow scheduler' 

2. In a web browser, type the following: \<public-IP-of-EC2>\:8080

***Output***
The code creates the following directories:
i. data - Stores the data pulled from S3.
ii. added_data - Data that has been added to the MySQL table.
iii. logs - Stores the logs of the process.

