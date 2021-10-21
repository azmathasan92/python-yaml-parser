# Python YAML Parser

Python YAML parser is a simple program that using jinja2 templating to parse any config into YAML at run time, This is very useful when you want to play with runtime configuration. Mostly it is useful while K8 deployment in the pipeline.

## Prequisite
1. Python2
2. Pip2
3. PyYAML [pip2 install PyYAML]
4. Jinja2 [pip2 install Jinja2]

## How to Run:
1. `cd devops-recipe-python-yaml-parser`
2. `python2 yaml_parse_vars.py --config config.yaml --template template.j2 -o deployment.yaml`
3. `cat deployment.yaml`

