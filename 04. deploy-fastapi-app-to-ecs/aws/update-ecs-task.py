import sys
import json
import argparse

parser = argparse.ArgumentParser('Replaces image in the task definition')
parser.add_argument('image', metavar='I', type=str, nargs='+')

args = parser.parse_args()

task_definition = json.load(sys.stdin)['taskDefinition']

task_definition['containerDefinitions'][0]['image'] = args.image[0]

try:
    task_definition['containerDefinitions'][1]['image'] = args.image[0]
except IndexError:
    pass # scheduler service have single container definition. So skip for index 1

delete_keys = ['taskDefinitionArn', 'revision', 'status', 'requiresAttributes', 'compatibilities', 'registeredAt', 'registeredBy']
all(task_definition.pop(key) for key in delete_keys)
print (json.dumps(task_definition))
