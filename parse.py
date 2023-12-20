#!/usr/bin/env python3

import json

from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('templates'))

with open('output.json', 'r') as f:
    findings = json.loads(f.read())
    findings = findings[0:10]
    print(len(findings))
    template = env.get_template('home.html')
    output_from_parsed_template = template.render(findings=findings)
    with open('index.html', 'w') as fh:
        fh.write(output_from_parsed_template)
