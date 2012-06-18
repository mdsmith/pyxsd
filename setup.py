#!/usr/bin/env python

from distutils.core import setup

try:    # Thanks to the ElementTree library (http://www.effbot.org/zone/element-index.htm)
    import cElementTree as ET
except:
     try:
          from xml.etree import cElementTree as ET
     except:
          try:
               from xml.etree import ElementTree as ET
          except:
               try:
                    import elementtree.ElementTree as ET
               except:
                    raise ImportError, "Your system needs the ElementTree or cElementTree library in order to run this package"
LongDescription = """\
pyXSD maps xml and xsd(XML Schema) files into python,
allowing for easy schema-based validation and transformation of xml files."""

setup(name             = "pyxsd",
      version          = '0.1',
      description      = "Python XML/Schema processing tool",
      long_description = LongDescription,
      author           = "Karl Norby and Michael Summers",
      author_email     = "knorby@uchicago.edu and summersms@ornl.gov",
      maintainer       = "Karl Norby",
      maintainer_email = "knorby@uchicago.edu",
      url              = "http://pyxsd.org",
      license          = "BSD License",
      packages         = ['pyxsd','pyxsd.elementRepresentatives',
                          'pyxsd.transforms', 'pyxsd.writers'],
      scripts          = ['scripts/pyXSD.py'],
      platforms        = "Python 2.3 or later. requires cElementTree or ElementTree. OS independent.",
      classifiers      = ['Topic :: Text Processing :: Markup :: XML',
                          'Programming Language :: Python',
                          'Operating System :: OS Independent',
                          'License :: OSI Approved :: BSD License',
                          'Intended Audience :: Science/Research',
                          'Development Status :: 4 - Beta'],)






