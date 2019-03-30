from lxml import etree

with open("show_security_zones.xml","r") as input_file:
    show_security = etree.fromstring(input_file.read())


#Ex-1a
print(show_security)
print(type(show_security))

#Ex-1b
print(etree.tostring(show_security).decode())

#Ex-1c
print("\nroot tag:",show_security.tag)
print("\nNumber of children of root element:",len(show_security.getchildren()))

#Ex-1d
print("\nFirst child element using method:",show_security.getchildren()[0].tag)
print("\nFirst child element using indices:",show_security[0].tag)

#Ex-1e
trust_zone = show_security.getchildren()[0]
print("\nText of zones-security-child",trust_zone.find("zones-security-zonename").text)


#Ex-1f
print("\nTags of child elements of trust_zone")
for child in trust_zone.getchildren():
    print(child.tag)
