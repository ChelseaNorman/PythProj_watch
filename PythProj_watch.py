import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        iframe_link = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if iframe_link:
            split_iframe_link = iframe_link.groups()
            return "https://youtu.be/" + split_iframe_link[3]
    else:
        return "None"

if __name__ == "__main__":
     main()