from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".","./templates"])


my_vars=[
{
    "vrf_name":"blue",
    "rd_number":"100:1",
    "ipv4_enabled":True,
    "ipv6_enabled":False
},
{
    "vrf_name":"red",
    "rd_number":"200:1",
    "ipv4_enabled":True,
    "ipv6_enabled":False
},
{
    "vrf_name":"yellow",
    "rd_number":"300:1",
    "ipv4_enabled":True,
    "ipv6_enabled":True
},
{
    "vrf_name":"green",
    "rd_number":"400:1",
    "ipv4_enabled":True,
    "ipv6_enabled":True
},
{
    "vrf_name":"black",
    "rd_number":"100:1",
    "ipv4_enabled":True,
    "ipv6_enabled":False
}
]

j2_input_vars={"my_vars": my_vars}
template_file = "ex4_class5_template.j2"
  
         
            
template = env.get_template(template_file)
#for vrf in len(my_vars): 

output=template.render(**j2_input_vars)

print(output)

