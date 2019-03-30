import xmltodict

xmlfile = open("show_security_zones.xml")
xmldata = xmlfile.read().strip()

my_xml = xmltodict.parse(xmldata)
print(my_xml)
print(type(my_xml))
for i,item in enumerate(my_xml['zones-information']['zones-security']):
    print(f"Security Zone #{i+1}: {item['zones-security-zonename']}")
