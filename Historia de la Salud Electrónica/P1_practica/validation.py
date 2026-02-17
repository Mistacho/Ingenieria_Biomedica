#apt-get install python3-lxml
from lxml import etree

xFileName = "Historia de la Salud Electrónica/P1_practica/ejemplo.xml"
sFileName = "Historia de la Salud Electrónica/P1_practica/ejemplo.xsd"

try:
    xDoc = etree.parse(xFileName)
    sDoc = etree.parse(sFileName)
    schema = etree.XMLSchema(sDoc)
    schema.assertValid(xDoc)
    print ("ok")
except etree.XMLSyntaxError as e:
    print (str(e))
except etree.XMLSchemaParseError as e:
    print (str(e))
except etree.DocumentInvalid as e:
    print (str(e))
