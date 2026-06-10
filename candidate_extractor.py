import re

def extract_name(text):

    lines = text.split("\n")

    for line in lines[:10]:

        line = line.strip()

        if len(line.split()) >= 2 and len(line.split()) <= 5:

            if "@" not in line and "phone" not in line.lower():

                return line

    return "Not Found"