import os
from block_markdown import markdown_to_html_node
import pathlib


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    print(f'dir_path_content = {dir_path_content}')
    
    files = os.listdir(dir_path_content)
    print(f'Listing files: {files}')

    for file in files:
        file_path = os.path.join(dir_path_content, file)
        print(f'file = {file_path}')
        if os.path.isdir(file_path):
            dest_dir_path = os.path.join(dest_dir_path, file)
            print(f"\n** Recursion {file_path} {template_path} -> {dest_dir_path}\n")
            generate_pages_recursive(file_path, template_path, dest_dir_path)

        elif os.path.isfile(file_path):
            dest_dir_path = os.path.join(dest_dir_path, "index.html")
            print(f"\n* Generating page: {file_path} {template_path} -> {dest_dir_path}\n")
            generate_page(file_path, template_path, dest_dir_path)
            print(f'Generated {file_path}')

