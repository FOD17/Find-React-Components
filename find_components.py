import re
import sys

def find_children(component_path):
    with open(component_path, 'r') as file:
        component_content = file.read()

    # Regular expression pattern to match React JS components
    pattern = r'<([A-Z]\w+)\s*[^>]*>(.*?)<\/\1>'

    # Find all matches in the component content
    matches = re.findall(pattern, component_content, re.DOTALL)

    children = []
    for match in matches:
        component_name = match[0]
        children.append(component_name)
        children.extend(find_children_recursively(match[1]))

    return children

def find_children_recursively(component_content):
    pattern = r'<([A-Z]\w+)\s*[^>]*>(.*?)<\/\1>'
    matches = re.findall(pattern, component_content, re.DOTALL)

    children = []
    for match in matches:
        component_name = match[0]
        children.append(component_name)
        children.extend(find_children_recursively(match[1]))

    return children

# Check if the component path is provided as an argument
if len(sys.argv) < 2:
    print("Please provide the absolute path of the React component as an argument.")
    sys.exit(1)

# Get the component path from the command-line argument
component_path = sys.argv[1]

# Find all children components
children = find_children(component_path)

if children:
    print("Children components:")
    for child in children:
        print(child)
else:
    print("No children components found.")
