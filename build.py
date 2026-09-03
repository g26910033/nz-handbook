import os

def build():
    sections = [
        "00-cover.html", "01-finance.html", "02-tickets.html",
        "03-nav.html", "04-stay.html", "05-klia.html",
        "06-prep.html", "07-safety.html", "08-north.html",
        "09-chch.html", "10-south.html", "11-aurora.html"
    ]
    
    with open("src/styles.css", "r", encoding="utf-8") as f:
        css_content = f.read().strip()
        
    css_blocks = css_content.split('/* --- STYLE_SPLIT --- */')
    styles_html = ""
    for block in css_blocks:
        styles_html += f"<style>\n{block.strip()}\n</style>"
        
    html = [
        '<!DOCTYPE html>\n<html lang="zh-Hant">\n<head>\n<meta charset="utf-8" />\n<meta name="viewport" content="width=device-width, initial-scale=1" />\n<title>紐西蘭冬季雙島自駕生存與財務教戰手冊｜2026冬季版</title>',
        styles_html + '</head>\n<body>\n<main class="book">'
    ]
    
    for sec in sections:
        with open(os.path.join("src", "sections", sec), "r", encoding="utf-8") as f:
            html.append(f.read().strip())
            
    html.append('</main>\n</body>\n</html>')
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write("\n".join(html) + "\n")

if __name__ == "__main__":
    build()
