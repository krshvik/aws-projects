import boto3
mc = boto3.client('elasticache')
response = mc.create_cache_cluster(
    CacheClusterId='test-1',
    AZMode='single-az',
    PreferredAvailabilityZone='us-east-2a',
    NumCacheNodes=1,
    Port=1230,
    AutoMinorVersionUpgrade=False,
    Engine='Memcached',
    CacheNodeType = 'cache.t2.micro'
)
print(response)