import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Make gap bigger
text = text.replace(
    '<div class="deployment-container" style="display: flex; flex-direction: row; gap: 1.5rem; justify-content: center; align-items: stretch; margin-top: 1.5rem; width: 100%; max-width: 1400px; margin-left: auto; margin-right: auto; text-align: left;">',
    '<div class="deployment-container" style="display: flex; flex-direction: row; gap: 2.5rem; justify-content: center; align-items: stretch; margin-top: 1.5rem; width: 100%; max-width: 1400px; margin-left: auto; margin-right: auto; text-align: left;">'
)

# Expand width and center vertically 
text = text.replace(
    '<div class="left-col" style="flex: 0 0 340px; display: flex; flex-direction: column;">',
    '<div class="left-col" style="flex: 0 0 540px; display: flex; flex-direction: column; justify-content: center;">'
)

# Increase font size for Mapping run to match the new size slightly
text = text.replace(
    '<p class="deployment-label" style="font-weight: 600; margin-bottom: 0.5rem; font-size: 1.1rem; color: var(--text-primary);">Mapping run</p>',
    '<p class="deployment-label" style="font-weight: 600; margin-bottom: 0.75rem; font-size: 1.25rem; color: var(--text-primary);">Mapping run</p>'
)

# Increase max-height constraint slightly if any, wait, it has flex-grow: 1, so it scales nicely based on width now.
# Give the mapping run card slightly more padding
text = text.replace(
    '<article class="deployment-card mappingrun-card" style="background: var(--background-primary); border: 1px solid var(--border-color); border-radius: 14px; padding: 0.75rem; box-shadow: var(--shadow-md); display: flex; flex-direction: column;">',
    '<article class="deployment-card mappingrun-card" style="background: var(--background-primary); border: 1px solid var(--border-color); border-radius: 16px; padding: 1.25rem; box-shadow: var(--shadow-md); display: flex; flex-direction: column;">'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
