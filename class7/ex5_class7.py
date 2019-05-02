from lxml import etree

with open("show_version.xml", "rb") as input_file:
    show_security = etree.fromstring(input_file.read())

print("NS maps:", show_security.nsmap)


output = show_security.find(".//{*}proc_board_id")
print("\nproc_board_id:", output.text)
