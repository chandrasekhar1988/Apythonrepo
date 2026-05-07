import boto3

# S3 రిసోర్స్‌ను క్రియేట్ చేయడం
s3 = boto3.resource('s3')

# 1. కొత్త బకెట్ క్రియేట్ చేయడం
bucket_name = "devops-chandra-bucket-2026" # పేరు యూనిక్‌గా ఉండాలి
try:
    s3.create_bucket(Bucket=bucket_name, 
                     CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
    print(f"బకెట్ '{bucket_name}' విజయవంతంగా క్రియేట్ చేయబడింది.")
except Exception as e:
    print(f"Error: {e}")

# 2. మీ అకౌంట్‌లో ఉన్న అన్ని బకెట్ల పేర్లు చూడటం
print("\nప్రస్తుతం ఉన్న బకెట్ల జాబితా:")
for bucket in s3.buckets.all():
    print(f"- {bucket.name}")


    