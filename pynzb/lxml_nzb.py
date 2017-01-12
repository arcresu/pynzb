from pynzb.base import BaseETreeNZBParser, NZBFile, NZBSegment

try:
    from lxml import etree
except ImportError:
    raise ImportError("You must have lxml installed before you can use the " +
        "lxml NZB parser.")

import sys
if sys.version_info.major < 3:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
    def as_io(xml): return StringIO(xml)
else:
    from io import BytesIO
    def as_io(xml): return BytesIO(bytes(xml, 'utf-8'))

class LXMLNZBParser(BaseETreeNZBParser):
    def get_etree_iter(self, xml, et=etree):
        return iter(et.iterparse(as_io(xml), events=("start", "end")))
