import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe[^>]*\bsrc="(https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+))"'
    match=re.search(pattern, s)

    if not match:
        return None

    video_id =match.group(2)
    return f"https://youtu.be/{video_id}"



if __name__ == "__main__":
    main()
