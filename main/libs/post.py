import re
from typing import List

def extract_tags(post_content: str)-> List[str]:
    # define regular expression pattern to match hashtags
    pattern = r'#\w+'
    # find all matches in the content
    matches = re.findall(pattern, post_content)
    # remove the "#" character from each match
    tags = [match[1:] for match in matches]
    # return the list of tags
    return tags