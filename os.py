import os
ret = os.access("/tmp/foo.txt", os.F_OK)
print "F_OK - return value %s"% ret
