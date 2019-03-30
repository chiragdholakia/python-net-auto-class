import xmltodict

def load_xml(filename):
    with open(filename,"r") as xmlfile:
        xmldata = xmlfile.read().strip()
    my_xml = xmltodict.parse(xmldata)
    return my_xml


def load_xml_forceList(filename,element):
    with open(filename,"r") as xmlfile:
        xmldata = xmlfile.read().strip()
    my_xml = xmltodict.parse(xmldata,force_list={element: True})
    return my_xml



if __name__ == "__main__":
    filename = "show_security_zones.xml"
    xmlfile1 = load_xml(filename)

    filename = "show_security_zones_single_trust.xml"
    xmlfile2 = load_xml(filename)
    xml_element ='zones-security'
    xmlfile3 = load_xml_forceList(filename,xml_element)

    print (xmlfile1)
    print ("\n\n\n")
    print (xmlfile2)


    print(type(xmlfile1 ['zones-information']['zones-security']))
    print(type(xmlfile2 ['zones-information']['zones-security']))
    print(type(xmlfile3 ['zones-information']['zones-security']))

