from textnode import TextNode, TextType
from copy_files import copy_files


def main():
  source = '/home/alex/workspace/github.com/SpottedHorse/static_site_generator/static'
  dest = '/home/alex/workspace/github.com/SpottedHorse/static_site_generator/public'
  
  copy_files(source, dest)

main()