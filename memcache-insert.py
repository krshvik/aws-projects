import memcache

for port in (11211,11211):
    print( "Testing memcached on port %d" % port)
    mc = memcache.Client(['test.yohf5f.0001.use2.cache.amazonaws.com:%d' % port])

    if mc.set('value1', 'value2'):
        print("stored key value pair")
        if mc.get('value1') == 'value2':
            print ("successfully retrieved value")
            print(mc.get('value1'))
            break
        else:
            print ("Failed to retrieve value")
    else:
        print( "Failed to store key value pair")
