#!/bin/env python3
import requests
import re
from lxml import etree
from urllib.parse import urlparse

domain = input("Please enter a URL: ")
print()
domains = set()
html = requests.get(domain).text
s = re.findall(r'http[^\/]{1,2}//([^(\/| |")]+)', html)
print(set(s))
print()
