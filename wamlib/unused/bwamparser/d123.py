import bwamparser
import csv
import uno
import unohelper
import string
import re
import datetime
import sys
import logging
import os
sys.path.append("..")
import bwam
import AbstractWAM

#      Copyright 2008-2010 eGovMon
#      This program is distributed under the terms of the GNU General
#      Public License.
#
#  This file is part of the eGovernment Monitoring
#  (eGovMon)
#
#  eGovMon is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  eGovMon is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with eGovMon; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston,
#  MA 02110-1301 USA


"""
Extract BWAM info from D3.2.1
"""
__author__="Nils Ulltveit-Moe"
__maintainer__="Nils Ulltveit-Moe"
__version__ = "$Revision$"
__updated__ = "$LastChangedDate$"

# Do not autogenerate WAMs that are hardcoded in bwam.py
HardcodedBWAMs=[c({}).wamid for c in AbstractWAM.d['instance'].getKlasses()]

UNORES="com.sun.star.bridge.UnoUrlResolver"
UNORESID="uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext"

try:
    file=sys.argv[1]
except (OIError,IntexError):
    print "Use:"
    print "Start OpenOffice with argument:"
    print 'soffice "-accept=socket,host=localhost,port=2002;urp;"'
    print ""
    print "python d123.py D3.2.1-FINAL-v1.0.odt >../autobwam.py"
    sys.exit(1)

# Insert things into openoffice spreadsheet
compctx = uno.getComponentContext()
resolver = compctx.ServiceManager.createInstanceWithContext(UNORES,compctx)
ctx=resolver.resolve(UNORESID)
smgr=ctx.ServiceManager
desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",ctx)
model = desktop.getCurrentComponent()


cwd = unohelper.systemPathToFileUrl( os.getcwd() )
fileUrl = unohelper.absolutize( cwd, unohelper.systemPathToFileUrl(file) )

doc = desktop.loadComponentFromURL(fileUrl,"_blank",0,())
parser=bwamparser.BwamParser()

print """#! /usr/bin/env python
# -*- coding: utf-8 -*-
\"\"\"
NOTE autobwam.py is automatically generated. Do not edit this file by hand!

To regenerate the file, run:

cd $EIAOHOME/robacc/WAMs/wamlib/bwamparser
python d123.py D3.2.1-FINAL-v1.0.odt > ../autobwam.py

autobwam.py implements all B-WAM rules except two in D3.2.1 automatically.

All BWAM classes inherits from AbstractB, which defines the list of WAMs.
\"\"\"
#      Copyright 2005, 2006 EIAO Consoritum
#      This program is distributed under the terms of the GNU General
#      Public License.
#
#  This file is part of the European Internet Accessibility Observatory
#  (EIAO)
#
#  EIAO is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  EIAO is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with EIAO; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston,
#  MA 02110-1301 USA
__author__     = "Annika Nietzio, Nils Ulltveit-Moe"
__maintainer__ = "Nils Ulltveit-Moe"
__version__    = "$Id: bwam.py 2375 2006-07-29 14:14:56Z anand $"

from AbstractWAM import *
import re
import bwam

"""

for i in range(16,doc.TextTables.Count):
   table=doc.TextTables.getByIndex(i)
   try:
      type=table.DataArray[0][0]
   except:
      continue
   if type=="B":
      # BWAM found
      # Parse formal description
      formalDescription=table.DataArray[6][1].encode('utf-8')
      try:
         res=parser.parse(formalDescription) 
      except bwamparser.BWAMParseError,e:
         sys.stderr.write("Parse error in "+str(formalDescription)+"\n\n")
         sys.stderr.write(str(e)+"\n\n")
         continue
      # Do not generate WAMs already present in bwam.py
      if parser.bwamid in HardcodedBWAMs:
         continue
      print "class %s(AbstractB):" % "_".join(parser.bwamid.split("."))
      print "   def __init__(self,awamresult):"
      print '      """'
      print "      %s" % table.DataArray[0][1].encode("utf-8")
      print
      print "      %s" % table.DataArray[1][0].encode("utf-8")
      print "      %s" % "\n      ".join(table.DataArray[1][1].encode("utf-8").split("\n"))
      print
      print "      %s: %s" % (table.DataArray[2][0].encode("utf-8"),table.DataArray[2][1].encode("utf-8"))
      print
      print "      %s: %s" % (table.DataArray[7][0].encode("utf-8"),table.DataArray[7][1].encode("utf-8"))
      print '      """'
      print "      AbstractB.__init__(self,awamresult,\"%s\",[" % (parser.bwamid)
      for awam in parser.awams:
          print "          '%s'," %  (awam)
      print "      ])" 
      print "      self.title = '%s'" % table.DataArray[4][1]
      print "      self.description = \"\"\"%s\"\"\"" % table.DataArray[2][1]
      print
      print "   def result(self,s):"
      print "      return ",res
      print
      print 'AppendKlass(%s)' % ("_".join(parser.bwamid.split(".")))
      print


