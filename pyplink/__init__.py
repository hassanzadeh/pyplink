"""A module to read Plink's binary files."""

# This file is part of pyplink.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to Creative
# Commons, PO Box 1866, Mountain View, CA 94042, USA.


from .pyplink import *

try:
    from .version import pyplink_version as __version__
except ImportError:
    __version__ = None


__author__ = "Louis-Philippe Lemieux Perreault"
__copyright__ = "Copyright 2014 Louis-Philippe Lemieux Perreault"
__credits__ = ["Louis-Philippe Lemieux Perreault"]
__license__ = "Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)"
__version__ = "0.3"
__maintainer__ = "Louis-Philippe Lemieux Perreault"
__email__ = "louis-philippe.lemieux.perreault@statgen.org"
__status__ = "Development"
