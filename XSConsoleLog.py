# Copyright (c) Citrix Systems 2008. All rights reserved.
# xsconsole is proprietary software.
#
# Xen, the Xen logo, XenCenter, XenMotion are trademarks or registered
# trademarks of Citrix Systems, Inc., in the United States and other
# countries.

from XSConsoleBases import *
from XSConsoleLang import *

def XSLog(*inParams):
    pass
    
def XSLogOnce(*inParams):
    pass
    
def XSLogFailure(*inParams):
    logString = "\n".join( [ str(param) for param in inParams ] )
    Lang(Exception(logString)) # Translate an exception so the test harness will pick it up
        
