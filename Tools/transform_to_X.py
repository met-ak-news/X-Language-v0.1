# Deterministic rule-based transform from plain English to X shorthand (example)
import re

def transform(text: str) -> str:
    t = text.strip()
    t = re.sub(r"\s+", ' ', t)
    t = t.replace('"', '')
    # naive transformation: wrap in U "..."
    return 'U "' + t[:500] + '"'  # truncate for examples

if __name__ == '__main__':
    print(transform('Fetch latest posts about GPT models from Reddit'))
