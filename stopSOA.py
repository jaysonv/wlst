#### Created by Michel Schildmeijer

#
# Set some constants

MS1Name='soa_server2'
MS1Name='bam_server2'

from os import getenv
WL_DOMAIN=os.getenv('WL_DOMAIN')
execfile(WL_DOMAIN + '_properties.py'  # load domain specific constants


nmConnect(NMAdminUser, NMAdminUserPW, hostname, nmPort, WL_DOMAIN, WL_DOMAIN_DIR, nmType)

try:
 nmKill(MS1Name)
except:
 pass

disconnect()

