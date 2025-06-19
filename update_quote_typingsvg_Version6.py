import random
import urllib.parse
import re

# 读取名言
with open("QUOTES.txt", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

quote = random.choice(quotes)
encoded_quote = urllib.parse.quote(quote)

# 读取README
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

# 替换 Typing SVG 行中的占位符
new_readme = re.sub(
    r'<!--QUOTE_START-->.*?<!--QUOTE_END-->',
    f'<!--QUOTE_START-->{encoded_quote}<!--QUOTE_END-->',
    readme,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)