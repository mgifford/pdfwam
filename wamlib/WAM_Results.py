# -- coding: utf-8
#
# Copyright (C) Tingtun AS 2013.
# 

"""
WAM_Results.py contains WAM result objects, generated by the WAMs,
and utility methods and constants used for generating EARL.
"""

__author__     = "Nils Ulltveit-Moe"
__updated__ = "$LastChangedDate$"
__version__    = "$Id$"

import string
import version
import pickle
import cgi


# Global assertion ID
assertionid=0

dumpfile=""

def setDumpFile(df):
   global dumpfile
   dumpfile=df
   try:
      loadAssertionId()
   except IOError:
      saveAssertionId()


def saveAssertionId():
   """
   Save EARL assertion ID.
   
   The WAM assertion ID is a sequence number that is unique to each WAM, and that is used to
   give a unique ID to EARL assertions, test requirements etc. 
   
   The assertion ID is saved in dumpfile.
   """
   global assertionid

   try:
      f=open(dumpfile,"w")
      pickle.dump(assertionid,f)
      f.close()
   except Exception, e:
      print 'Error saving Assertion ID',e
      pass

def loadAssertionId():
   """
   Load saved assertion ID from dumpfile.

   The WAM assertion ID is a sequence number that is unique to each WAM, and that is used to
   give a unique ID to EARL assertions, test requirements etc. 
   """
   global assertionid
   f=open(dumpfile)
   assertionid=pickle.load(f)
   f.close()

def setAssertionId(self,number=0):
   """
   Set assertion ID (for testing purposes)
   """
   global assertionid
   assertionid=number

# Global (default) test subject
_testSubject=None

def defaultTestSubject(subject):
   """
   Set default test subject for generated EARL.
   """
   global _testSubject
   _testSubject=subject

class htmlQuote:
   """
   HTML quoting class that works with 3store/RDF.
   """
   def __init__(self):
      """
      >>> h=htmlQuote()
      >>> h.quote("<test>&gml;'")
      '&lt;test&gt;&gml;gml;&quot;'
      """
      self.map={"<":"&lt;",
                ">":"&gt;",
                "&":"&gml;",
                "'":"&quot;",
                '"':"&quot;"}
   def htmlQuoteChar(self,s):
      """
      Quote one HTML character.
      """
      try:
         return self.map[s]
      except KeyError:
         return s
   def quote(self,s):
      """
      Quote a HTML string.
      """
      return cgi.escape(string.join([self.htmlQuoteChar(c) for c in s],''))

# Consider to parse the WAM IDs, to provide the individual data needed
# by the ETL. (At least provide this as a service.)
"""
EIAO ids
"""
EIAO_NS=u"http://www.eiao.net/rdf/2.0/"
EGOVMON_NS="http://www.egovmon.no/rdf/2.0/"

#XMLBASE=EIAO_NS+u"#"
XMLBASE=EGOVMON_NS+u"#"

# WAM types
BWAM=0
LANGUAGE=1
TECHNOLOGY=2
INTLINK=3
EXTLINK=4
MEDIATYPE=5
VERSION=6
CREATOR=7
PRODUCER=8
TITLE=9
AUTHOR=10
VERSION=11
CREATION_TIME=12
MODIFICATION_TIME=13

egovmonMwamId={
LANGUAGE   : "EGOVMON.LANG.1.2",
TECHNOLOGY : "EGOVMON.TECH.1.2",
INTLINK    : "EGOVMON.INT.1.2",
EXTLINK    : "EGOVMON.EXT.1.2",
MEDIATYPE  : "EGOVMON.MEDIA.1.2",
VERSION    : "EGOVMON.VER.1.2",
CREATOR    : "EGOVMON.CRE.1.2",
PRODUCER   : "EGOVMON.PROD.1.2",
TITLE      : "EGOVMON.TITLE.1.2",
AUTHOR     : "EGOVMON.AUTR.1.2",
CREATION_TIME: "EGOVMON.CTIME.1.2",
MODIFICATION_TIME : "EGOVMON.MTIME.1.2"
}

egovmonMwamDict={
LANGUAGE   : EGOVMON_NS+u"#language",
TECHNOLOGY : EGOVMON_NS+u"#technology",
INTLINK    : EGOVMON_NS+u"#internalLinks",
EXTLINK    : EGOVMON_NS+u"#externalLinks",
MEDIATYPE  : EGOVMON_NS+u"#mediaType",
VERSION    : EGOVMON_NS+u"#version",
CREATOR    : EGOVMON_NS+u"#creator",
PRODUCER   : EGOVMON_NS+u"#producer",
TITLE      : EGOVMON_NS+u"#title",
AUTHOR     : EGOVMON_NS+u"#author",
CREATION_TIME: EGOVMON_NS+u"#ctime",
MODIFICATION_TIME: EGOVMON_NS+u"mtime"
}

"""
UWEM information
"""

"""
UWEM id
"""
UWEM_Id=u"UWEM 1.0 test suite"

"""
EARL information
"""

EARL_NS =       u"http://www.w3.org/WAI/ER/EARL/nmg-strawman"

"""
EARL test mode
"""

MANUAL    = 0
AUTOMATIC = 1
HEURISTIC = 2

earlModeDict={
MANUAL    : EARL_NS+u"#manual",
AUTOMATIC : EARL_NS+u"#automatic",
HEURISTIC : EARL_NS+u"#heuristic"}

"""
EARL validity level
"""

PASS          = 0
FAIL          = 1 # indicates barrier
CANNOTTELL    = 2
NOTAPPLICABLE = 3
NOTTESTED     = 4

earlValidityDict = {
PASS          : EARL_NS+u"#pass",
FAIL          : EARL_NS+u"#fail",
CANNOTTELL    : EARL_NS+u"#cannotTell",
NOTAPPLICABLE : EARL_NS+u"#notApplicable",
NOTTESTED     : EARL_NS+u"#notTested"}

"""
EARL confidence level
"""

HIGH   = 0
MEDIUM = 1
LOW    = 2

earlConfidenceDict={
HIGH          : EARL_NS+u"#high",
MEDIUM        : EARL_NS+u"#medium",
LOW           : EARL_NS+u"#low"}

"""
EARL test subject types
"""

TESTSUBJECT = 0
SOFTWARE    = 1
WEBCONTENT  = 2


# Class for WAM test results. Contains all necessary data for the EARL assertions
class WAM_Results:
   def __init__(self,wamid,title,description,type=BWAM,result=CANNOTTELL,line=0,column=0,mode=AUTOMATIC,prob=None,message=None,xhtml=""):

      self.type=type

      # BWAM ID with version
      # Replace : with . in WAM ID to make legal URLs
      self.bwamVersionedId=wamid
         
      self.bwamName=wamid

      # BWAM ID without version
      self.bwamId=".".join(self.bwamVersionedId.split(".")[:-1])

      if type==BWAM:
         # BWAM description
         self.description=description

         # Title
         self.title=title

      #Message from the WAM, typically an example of the error
      self.message = message

      # Version of WAM
      self.version=self.bwamVersionedId.split(".")[-1]
      
      # Test result
      self.result=result

      # Line number of test result
      self.line=line

      # Column number of test result
      self.column=column

      # XHTML from the test result
      self.xhtml = xhtml

      # Assertion ID for EARL
      self.assertionId=self._nextAssertionId()

      # Assertion mode
      self.mode=mode

      # Probability - Only applicable for heuristic tests
      self.prob=prob

      # Default RDF host ID (from wamid URL, with '.' instead of '/')
      # E.g: http://www.eiao.net/1.0/RelaxedWAM 
      # is converted to www.eiao.net.1.0.RelaxedWam
      self.rdfhostid=string.join([i for i in version.wamid.split("/")[1:] if i!=''],'.')

      self.htmlQuoter=htmlQuote()

      #Message from the WAM, typically an example of the error
      try:
         self.message = self.htmlQuoter.quote(message)
      except:
         pass


   def _nextAssertionId(self):
      """
      Return next assertion ID (private method)
      Depends on the Python GIL (Global Interpreter Lock)
      to be thread safe. 
      """
      global assertionid
      assertionid=assertionid+1
      return assertionid


   def earlAssertionId(self):
      """
      Assertion ID

      Context:
      <earl:Assertion rdf:ID="thisID">

      """
      return string.join([self.rdfhostid,self.bwamVersionedId+"-A"+str(self.assertionId)],".")

   def earlAssertedBy(self):
      """
      Asserted by

      Context:
      <earl:Assertion>
         <earl:assertedBy rdf:resource=thisId/>

      """
      return version.wamid

   def earlVersion(self):
      """
      EARL version number
      """
      return self.version

   def earlSubject(self):
      """
      EARL:Subject
      """
      return _testSubject

   def earlRequirementId(self):
      """
      Test case ID.
      
      Context: 
      <earl:Requirement rdf:ID=thisId>
      <earl:Assertion>
         <earl:requirement rdf:resource=thidId/>

      """
      return self.bwamVersionedId

   def earlTestcaseTitle(self):
      """
      Title of test suite
      
      Context:
      <earl:TestCase>
         <dc:title>

      """
      return self.bwamName
      
   def earlDescription(self):
      """
      Description of test case
      Context:
      <earl:TestCase>
         <dc:description>Missing ALT attribute</dc:description> 

      Returns description (e.g. Missing ALT attribute).

      """
      return self.htmlQuoter.quote(self.description)

   def earlMode(self):
      """
      earl:mode (#automatic)

      """
      return earlModeDict[self.mode]

   def earlResult(self):
      """
      earl:result

      """
      return earlValidityDict[self.result]

   def earlValidityId(self):
      """
      Generate unique ID for earl:validity

      """
      return string.join([self.rdfhostid,self.bwamVersionedId+"-V"+str(self.assertionId)],".")

   def earlMessage(self):
      """
      Message of assertion
      """
      return self.message

   def eiaoSingleLocationId(self):
      """
      Generate unique ID for earl:singleLocation
      """
      return string.join([self.rdfhostid,self.bwamVersionedId+"-L"+str(self.assertionId)],".")

   def eiaoLine(self):
      """
      Line number of assessment result
      """
      return self.line

   def eiaoColumn(self):
      """
      Column number of assessment result
      """
      return self.column

   def eiaoMetaDataId(self):
      """
      Generate unique ID for earl:MetaData
      """
      return string.join([self.rdfhostid,self.bwamVersionedId+"-M"+str(self.assertionId)],".")

   def eiaoValue(self):
      """
      MWAM result
      """
      return self.result

   def eiaoType(self):
      """
      Type of MWAM meta data
      """
      # return eiaoMwamDict[self.type]
      return egovmonMwamDict[self.type]      

if __name__ == "__main__":
   import doctest
   doctest.testmod()
