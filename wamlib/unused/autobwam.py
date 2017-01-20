#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
NOTE autobwam.py is automatically generated. Do not edit this file by hand!

To regenerate the file, run:

cd $EIAOHOME/robacc/WAMs/wamlib/bwamparser
python d123.py D3.2.1-FINAL-v1.0.odt > ../autobwam.py

autobwam.py implements all B-WAM rules except two in D3.2.1 automatically.

All BWAM classes inherits from AbstractB, which defines the list of WAMs.
"""

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


__author__     = "Annika Nietzio, Nils Ulltveit-Moe"
__updated__ = "$LastChangedDate$"
__version__    = "$Id: bwam.py 2375 2006-07-29 14:14:56Z anand $"

from AbstractWAM import *
import re
import bwam


class UWEM_B_10_1_1_3_HTML_DEF_1_1(AbstractB):
   def __init__(self,awamresult, **args):
      """
      UWEM.B.10.1.1.3.HTML.DEF.1.1 – Non-text content without alt attribute

      History
      Initial version
      FTB
      2006-09-28

      WCAG 1.0 reference: Checkpoint 1.1: Provide a text equivalent for every non-text element (e.g., via "alt", "longdesc", or in element content). This includes: images, graphical representations of text (including symbols), image map regions, animations (e.g., animated GIFs), applets and programmatic objects, ascii art, frames, scripts, images used as list bullets, spacers, graphical buttons, sounds (played with or without user interaction), stand-alone audio files, audio tracks of video, and video. [Priority 1]

      Mode: Fully automatable.
      """
      AbstractB.__init__(self,awamresult,"UWEM.B.10.1.1.3.HTML.DEF.1.1",[
          'EIAO.A.10.1.1.2.HTML.1.1',
      ], **args)
      self.title = 'The inspected non-text content element does not have an alt attribute.'
      self.description = """Checkpoint 1.1: Provide a text equivalent for every non-text element (e.g., via "alt", "longdesc", or in element content). This includes: images, graphical representations of text (including symbols), image map regions, animations (e.g., animated GIFs), applets and programmatic objects, ascii art, frames, scripts, images used as list bullets, spacers, graphical buttons, sounds (played with or without user interaction), stand-alone audio files, audio tracks of video, and video. [Priority 1]"""

   def result(self,s):
      return  1 - int(self.aWAM("EIAO.A.10.1.1.2.HTML.1.1",s))

AppendKlass(UWEM_B_10_1_1_3_HTML_DEF_1_1)

class UWEM_B_10_3_5_3_HTML_DEF_3_1(AbstractB):
   def __init__(self,awamresult, **args):
      """
      UWEM.B.10.3.5.3.HTML.DEF.3.1 – Heading level skipped

      History
      Version based on D3.1.1.
      FTB
      2006-09-27

      WCAG 1.0 reference: Checkpoint 3.5: Use header elements to convey document structure and use them according to specification. [Priority 2]

      Mode: Fully automatable.
      """
      AbstractB.__init__(self,awamresult,"UWEM.B.10.3.5.3.HTML.DEF.3.1",[
          'EIAO.A.10.3.5.1.HTML.2.1',
      ], **args)
      self.title = 'The inspected heading element (<h1>, <h2>, ...) skips one or more levels in the heading structure.'
      self.description = """Checkpoint 3.5: Use header elements to convey document structure and use them according to specification. [Priority 2]"""

   def result(self,s):
      return  int(self.aWAM("EIAO.A.10.3.5.1.HTML.2.1",s))

AppendKlass(UWEM_B_10_3_5_3_HTML_DEF_3_1)

class UWEM_B_10_9_1_3_HTML_DEF_1_1(AbstractB):
   def __init__(self,awamresult, **args):
      """
      UWEM.B.10.9.1.3.HTML.DEF.1.1 – Server-side image map

      History
      Initial version
      FTB
      2006-09-28

      WCAG 1.0 reference: Checkpoint 9.1: Provide client-side image maps instead of server-side image maps except where the regions cannot be defined with an available geometric shape. [Priority 1]

      Mode: Fully automatable.
      """
      AbstractB.__init__(self,awamresult,"UWEM.B.10.9.1.3.HTML.DEF.1.1",[
          'EIAO.A.10.9.1.2.HTML.1.1',
      ], **args)
      self.title = 'The inspected image is used as server-side image map.'
      self.description = """Checkpoint 9.1: Provide client-side image maps instead of server-side image maps except where the regions cannot be defined with an available geometric shape. [Priority 1]"""

   def result(self,s):
      return  int(self.aWAM("EIAO.A.10.9.1.2.HTML.1.1",s))

AppendKlass(UWEM_B_10_9_1_3_HTML_DEF_1_1)

class UWEM_B_10_11_2_3_HTML_DEF_1_1(AbstractB):
   def __init__(self,awamresult, **args):
      """
      UWEM.B.10.11.2.3.HTML.DEF.1.1 – Use of deprecated element

      History
      Version based on D3.1.1.
      FTB
      2006-09-28

      WCAG 1.0 reference: Checkpoint 11.2: Avoid deprecated features of W3C technologies.[Priority 2]

      Mode: Fully automatable.
      """
      AbstractB.__init__(self,awamresult,"UWEM.B.10.11.2.3.HTML.DEF.1.1",[
          'EIAO.A.10.11.2.1.HTML.1.1',
      ], **args)
      self.title = 'The inspected element is deprecated in HTML 4.01.'
      self.description = """Checkpoint 11.2: Avoid deprecated features of W3C technologies.[Priority 2]"""

   def result(self,s):
      return  int(self.aWAM("EIAO.A.10.11.2.1.HTML.1.1",s))

AppendKlass(UWEM_B_10_11_2_3_HTML_DEF_1_1)

class UWEM_B_10_11_2_3_HTML_DEF_2_1(AbstractB):
   def __init__(self,awamresult, **args):
      """
      UWEM.B.10.11.2.3.HTML.DEF.2.1 – Use of deprecated attribute

      History
      Initial version
      FTB
      2006-09-28

      WCAG 1.0 reference: Checkpoint 11.2: Avoid deprecated features of W3C technologies.[Priority 2]

      Mode: Fully automatable.
      """
      AbstractB.__init__(self,awamresult,"UWEM.B.10.11.2.3.HTML.DEF.2.1",[
          'EIAO.A.10.11.2.2.HTML.1.1',
      ], **args)
      self.title = 'The attribute of the inspected element is deprecated in HTML 4.01.'
      self.description = """Checkpoint 11.2: Avoid deprecated features of W3C technologies.[Priority 2]"""

   def result(self,s):
      return  int(self.aWAM("EIAO.A.10.11.2.2.HTML.1.1",s))

AppendKlass(UWEM_B_10_11_2_3_HTML_DEF_2_1)

class UWEM_B_10_12_1_3_HTML_DEF_1_1(AbstractB):
   def __init__(self,awamresult, **args):
      """
      UWEM.B.10.12.1.3.HTML.DEF.1.1 – <frame> or <iframe> without title

      History
      Initial version
      FTB
      2006-09-28

      WCAG 1.0 reference: Checkpoint 12.1: Title each frame to facilitate frame identification and navigation. [Priority 1]

      Mode: Fully automatable.
      """
      AbstractB.__init__(self,awamresult,"UWEM.B.10.12.1.3.HTML.DEF.1.1",[
          'EIAO.A.10.12.1.2.HTML.1.1',
      ], **args)
      self.title = 'The inspected <frame> or <iframe> element does not have a title attribute.'
      self.description = """Checkpoint 12.1: Title each frame to facilitate frame identification and navigation. [Priority 1]"""

   def result(self,s):
      return  not ( int(self.aWAM("EIAO.A.10.12.1.2.HTML.1.1",s)) )

AppendKlass(UWEM_B_10_12_1_3_HTML_DEF_1_1)

class UWEM_B_10_12_3_3_HTML_DEF_1_1(AbstractB):
   def __init__(self,awamresult, **args):
      """
      UWEM.B.10.12.3.3.HTML.DEF.1.1 – <fieldset> without <legend>

      History
      Version based on D3.1.1.
      FTB
      2006-09-28

      WCAG 1.0 reference: Checkpoint 12.3: Divide large blocks of information into more manageable groups where natural and appropriate. [Priority 2]

      Mode: Fully automatable.
      """
      AbstractB.__init__(self,awamresult,"UWEM.B.10.12.3.3.HTML.DEF.1.1",[
          'EIAO.A.10.12.3.1.HTML.1.1',
      ], **args)
      self.title = 'The inspected <fieldset> element does not contain a <legend> element.'
      self.description = """Checkpoint 12.3: Divide large blocks of information into more manageable groups where natural and appropriate. [Priority 2]"""

   def result(self,s):
      return  not ( int(self.aWAM("EIAO.A.10.12.3.1.HTML.1.1",s)) )

AppendKlass(UWEM_B_10_12_3_3_HTML_DEF_1_1)

class UWEM_B_10_12_3_3_HTML_DEF_4_1(AbstractB):
   def __init__(self,awamresult, **args):
      """
      UWEM.B.10.12.3.3.HTML.DEF.4.1 – <optgroup> without label

      History
      Version based on D3.1.1.
      FTB
      2006-09-28

      WCAG 1.0 reference: Checkpoint 12.3: Divide large blocks of information into more manageable groups where natural and appropriate. [Priority 2]

      Mode: Fully automatable.
      """
      AbstractB.__init__(self,awamresult,"UWEM.B.10.12.3.3.HTML.DEF.4.1",[
          'EIAO.A.10.12.3.1.HTML.2.1',
      ], **args)
      self.title = 'The inspected <optgroup> element does not have a label attribute.'
      self.description = """Checkpoint 12.3: Divide large blocks of information into more manageable groups where natural and appropriate. [Priority 2]"""

   def result(self,s):
      return  not ( int(self.aWAM("EIAO.A.10.12.3.1.HTML.2.1",s)) )

AppendKlass(UWEM_B_10_12_3_3_HTML_DEF_4_1)

class UWEM_B_10_12_4_3_HTML_DEF_1_1(AbstractB):
   def __init__(self,awamresult, **args):
      """
      UWEM.B.10.12.4.3.HTML.DEF.1.1 – Form control element without id

      History
      Version based on D3.1.1.
      FTB
      2006-09-28

      WCAG 1.0 reference: Checkpoint 12.4: Associate labels explicitly with their controls. [Priority 2]

      Mode: Fully automatable.
      """
      AbstractB.__init__(self,awamresult,"UWEM.B.10.12.4.3.HTML.DEF.1.1",[
          'EIAO.A.10.12.4.2.HTML.1.1',
      ], **args)
      self.title = 'The inspected form control element does not have an id attribute.'
      self.description = """Checkpoint 12.4: Associate labels explicitly with their controls. [Priority 2]"""

   def result(self,s):
      return  not ( int(self.aWAM("EIAO.A.10.12.4.2.HTML.1.1",s)) )

AppendKlass(UWEM_B_10_12_4_3_HTML_DEF_1_1)

class UWEM_B_10_12_4_3_HTML_DEF_2_1(AbstractB):
   def __init__(self,awamresult, **args):
      """
      UWEM.B.10.12.4.3.HTML.DEF.2.1 – Form control element without corresponding <label>

      History
      Version based on D3.1.1.
      FTB
      2006-09-28

      WCAG 1.0 reference: Checkpoint 12.4: Associate labels explicitly with their controls. [Priority 2]

      Mode: Fully automatable.
      """
      AbstractB.__init__(self,awamresult,"UWEM.B.10.12.4.3.HTML.DEF.2.1",[
          'EIAO.A.10.12.4.2.HTML.2.1',
      ], **args)
      self.title = 'Within the (X)HTML resource there is no <label> element with for attribute corresponding to the id of the inspected form control element.'
      self.description = """Checkpoint 12.4: Associate labels explicitly with their controls. [Priority 2]"""

   def result(self,s):
      return  not ( int(self.aWAM("EIAO.A.10.12.4.2.HTML.2.1",s)) )

AppendKlass(UWEM_B_10_12_4_3_HTML_DEF_2_1)
