from jinja2 import Template
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates"])
# input_template_file="ex2a_class5_template.j2"

# with open (input_template_file) as f:
# 	my_template=f.read()


input_vars_nxos1 = {
    "interf1": "Ethernet2/1",
    "ip1": "10.1.100.1",
    "netmask1": "24",
    "nei_ip": "100.1.100.2",
    "as_number": "22",
}
input_vars_nxos2 = {
    "interf1": "Ethernet2/1",
    "ip1": "10.1.100.2",
    "netmask1": "24",
    "nei_ip": "100.1.100.1",
    "as_number": "22",
}


for vars in [input_vars_nxos1, input_vars_nxos2]:
    input_template_file = "ex2b_class5_template.j2"
    template = env.get_template(input_template_file)
    output = template.render(**vars)

    print(output)
