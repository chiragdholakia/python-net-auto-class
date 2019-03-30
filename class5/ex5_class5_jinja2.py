from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)

env.loader = FileSystemLoader([".","./templates"])

j2_vars={
	"clock_timezone":"PST",
	"clock_offset":"-8",
	"clock_daylight":"PDT",
	"ntp1":"130.126.24.24",
	"ntp2":"152.2.21.1"
}

template_file = "ex5_class5_template.j2"

template = env.get_template(template_file)
output_cfg = template.render(**j2_vars)
print(output_cfg)



