import lxml.etree as ET
import os


def convert(input_xml, transformation, output_xml):
    if os.path.exists(output_xml):
        os.remove(output_xml)
    dom = ET.parse(input_xml)
    xslt = ET.parse(transformation)
    transform = ET.XSLT(xslt)
    result = transform(dom)
    infile = ET.tostring(result, pretty_print=True, encoding='unicode')
    outfile = open(output_xml, 'a')
    outfile.write(infile)


convert('input.xml', 'xslt_logic.xsl', 'output.xml')
