import boto3

s3 = boto3.resource('s3', region_name='us-east-1')
bucket_name = "devops-chandra-bucket-2026"

try:
    # us-east-1 కోసం CreateBucketConfiguration అవసరం లేదు
    s3.create_bucket(Bucket=bucket_name)
    print(f"బకెట్ '{bucket_name}' క్రియేట్ చేయబడింది.")
except Exception as e:
    print(f"Error: {e}")

# 2. మీ అకౌంట్‌లో ఉన్న అన్ని బకెట్ల పేర్లు చూడటం
print("\nప్రస్తుతం ఉన్న బకెట్ల జాబితా:")
for bucket in s3.buckets.all():
    print(f"- {bucket.name}")


    