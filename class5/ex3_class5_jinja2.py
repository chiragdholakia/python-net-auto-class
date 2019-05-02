from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates"])


my_vars = {
    "vrf_name": "blue",
    "rd_number": "100:1",
    "ipv4_enabled": True,
    "ipv6_enabled": False,
}

template_file = "ex3_class5_template.j2"
template = env.get_template(template_file)
output = template.render(**my_vars)

print(output)
