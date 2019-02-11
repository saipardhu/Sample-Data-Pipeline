#!/bin/bash

mysql -e "create database if not exists rescale"

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



for f in /home/ec2-user/rescale/data/*
do
    mysql -e "load data local infile '"$f"' into table rescale.spotprices fields TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES" 
    if [ $? == 0 ] ; then
       mv "$f" /home/ec2-user/rescale/added_data
    fi
done
