# HackerRank Problem about Parsing HTML code Part 1. Link: https://www.hackerrank.com/challenges/html-parser-part-1/problem
# Documentation of HTML Parser. Link: https://docs.python.org/3/library/html.parser.html
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        return
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if len(attrs) > 0:
            for i in range(len(attrs)):
                print(f"-> {attrs[i][0]} > {attrs[i][1]}")
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if len(attrs) > 0:
            for i in range(len(attrs)):
                print(f"-> {attrs[i][0]} > {attrs[i][1]}")

parser = MyHTMLParser()

lines = []
for _ in range(int(input())):
    lines.append(input())

for i in lines:
    parser.feed(i)


