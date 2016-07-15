# -*- coding: utf-8 -*-
import time,uuid
def next_id(t=None):
    '''
    Return next id as 50-char string.

    Args:
        t: unix timestamp, default to None and using time.time().
    '''
    if t is None:
        t = time.time()
    print t*1000
    print uuid.uuid4().hex
    return '%015d%s000' % (int(t * 1000), uuid.uuid4().hex)
    print t*1000
    print uuid.uuid4().hex

print next_id()