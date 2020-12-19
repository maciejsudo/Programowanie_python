#Maciej Sudol 303073
#Elektronika AGH 3 rok
import xml.sax
from xml.dom import minidom

#parsowanie z użyciem DOM:

DOMTree = minidom.parse("XML_example_file.xml")
Collection = DOMTree.documentElement

borrowers = Collection.getElementsByTagName("person")

print("\nPARSOWANIE Z UZYCIEM DOM: \n")

for person in borrowers:
    imie= person.getElementsByTagName("name")[0]
    print("imie kredytobiorcy:",imie.childNodes[0].data)

    wiek=person.getElementsByTagName("age")[0]
    print("wiek :", wiek.childNodes[0].data)

    plec=person.getElementsByTagName("gender")[0]
    print("płeć :", plec.childNodes[0].data)

    dlug=person.getElementsByTagName("debts")[0]
    print("dług :", dlug.childNodes[0].data,"\n")

#parsowanie z użyciem SAX:

print("PARSOWANIE Z UZYCIEM SAX: \n")


class Credit(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ""

    def startElement(self, tag, attributes):
        self.currentdata = tag

    def characters(self, content):
        if self.currentdata == "name":
            print("imie kredytobiorcy :", content)
        elif self.currentdata == "age":
            print("wiek : ", content)
        elif self.currentdata == "gender":
            print("płeć :", content)
        elif self.currentdata == "debts":
            print("dług :", content,"\n")

    def endElement(self, tag):
        self.currentdata = ""


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = Credit()
parser.setContentHandler(Handler)
parser.parse("XML_example_file.xml")



