#!/usr/bin/python
import jinja2, yaml, os, argparse, sys
import traceback, subprocess
unbuffered = os.fdopen(sys.stdout.fileno(), 'w', 0)
sys.stdout = unbuffered

def main(args):
    path, filename = os.path.split(args.template)
    templateFilePath = jinja2.FileSystemLoader(path)
    jinjaEnv = jinja2.Environment(loader=templateFilePath,trim_blocks=True)
    jTemplate = jinjaEnv.get_template(filename)
  
    with open(args.config) as config:
        config =  yaml.load(config, Loader=yaml.FullLoader)
    result=jTemplate.render(config)
    
    with open(args.output, 'w') as out:
        out.write(result)    

    return 0

def parseArgs():
    parser = argparse.ArgumentParser(description='Python template engine using jinja2')
    parser.add_argument('-c', '--config', type=str, required=True, help='Jija2 template configuration yaml file')
    parser.add_argument('-t', '--template', type=str, required=True, help='Jija2 template file')
    parser.add_argument('-o', '--output', type=str, required=True, help='Yaml output file')
    args = parser.parse_args()
    return args

args = parseArgs()
if __name__ == '__main__':
    exit(main(args))

