import boto3
import os
import pandas as pd

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('sample-spot-prices')
p_dir = '/home/ec2-user/rescale' #Parent directory
d_dir = p_dir + '/data'  #data directory
add_dir = p_dir + '/added_data'

#fnamess=[]

#Create the directories if not exists
if not os.path.exists(p_dir):
    os.mkdir(p_dir)

if not os.path.exists(d_dir):
    os.mkdir(d_dir)

if not os.path.exists(add_dir):
    os.mkdir(add_dir)


#Read the bucket and download all the csv files
for object in my_bucket.objects.all():
    if(object.key.endswith('.csv') and (not os.path.exists(d_dir+"/"+object.key) or (not os.path.exists(d_dir+"/"+object.key)))):
        #buckets.append(object.key)
        path, filename = os.path.split(object.key)
        print("Downloading the file {0}".format(object.key))
        my_bucket.download_file(object.key, d_dir+"/"+filename)
        data=pd.read_csv(d_dir+"/"+filename)
        acc_id = filename.split("_")[2]
        region = filename.split("_")[3].split(".")[0]
        data['Account_id']=acc_id
        data['Region']=region
        colnames=['Account_id','ProductDescription','InstanceType','AvailabilityZone','SpotPrice','Timestamp','Region']
        data.reindex(columns=colnames)
        data.to_csv(d_dir+"/"+filename,encoding='utf-8',index=False)
        #fnames.append(filename)
