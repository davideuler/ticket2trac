
import sys
import ticket2trac
import os

if len(sys.argv) <= 2:
    print "usage:python import2trac.py ticket.txt trac-install-path"
    sys.exit(1)

print "reading file", sys.argv[1]

ticketfile=sys.argv[1]
trac_install_path=sys.argv[2]

for line in open(ticketfile,"r"):
    print(line)
    sys.argv = [trac_install_path,line]
    print sys.argv
    os.system('python ticket2trac.py %s %s' % (trac_install_path,line) )