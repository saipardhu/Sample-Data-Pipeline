#!/bin/bash

#Create the database if not exits
mysql -e "create database if not exists rescale"

#Create the table with columns
mysql -e "CREATE TABLE IF NOT EXISTS rescale.spotprices
(
  ProductDescription varchar(50),
  InstanceType varchar(50),  
  AvailabilityZone VARCHAR(150),
  SpotPricerice  float(50),
  Timestamp datetime(5),
  Account_id int ,
  Region VARCHAR(50)
);"


#Read all the csv files from the data dir. and insert into the table and move it to the dir. added_data 
for f in /home/ec2-user/rescale/data/*
do
    mysql -e "load data local infile '"$f"' into table rescale.spotprices fields TERMINATED BY ',' LINES TERMINATED BY '\n'" 
    if [ $? == 0 ] ; then
       mv "$f" /home/ec2-user/rescale/added_data
    fi
done
