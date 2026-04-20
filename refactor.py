import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Remove Abstract section
abstract_pattern = r"<!-- Paper abstract -->.*?<!-- End paper abstract -->"
text = re.sub(abstract_pattern, "", text, flags=re.DOTALL)

# 2. Summary Section Layout
# Remove Summary title
text = re.sub(r'<h2 class="title is-3" style="margin-bottom: 2rem;">Summary</h2>\s*', "", text)

# Remove dashed borders and background from summary cards
# e.g.: background: rgba(250, 235, 215, 0.5); border: 2px dashed rgba(200, 150, 150, 0.5);
text = re.sub(r'background:\s*rgba\([^)]+\);\s*border:\s*2px dashed rgba\([^)]+\);\s*', '', text)

# 3. Real-world Deployment Layout
start_tag = '<h2 class="title is-3">Real-world Deployment</h2>'
end_tag = '<!-- Hall Environment Section -->'

start = text.find(start_tag)
end = text.find(end_tag)

if start != -1 and end != -1:
    section = text[start:end]
    
    articles = re.findall(r'<article.*?</article>', section, flags=re.DOTALL)
    
    if len(articles) == 5:
        # The first article is mapping run
        mapping = articles[0]
        # The rest are the 4 cards
        others = "\n".join(articles[1:])
        
        new_html = f'''<h2 class="title is-3">Real-world Deployment</h2>
          <div class="deployment-container" style="display: flex; flex-direction: row; gap: 1.5rem; justify-content: center; align-items: stretch; margin-top: 1.5rem; width: 100%; max-width: 1400px; margin-left: auto; margin-right: auto; text-align: left;">
            <div class="left-col" style="flex: 0 0 340px; display: flex; flex-direction: column;">
              {mapping}
            </div>
            <div class="right-col" style="flex: 1; display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
              {others}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  '''
        
        text = text[:start] + new_html + text[end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("HTML restructuring completed successfully.")
