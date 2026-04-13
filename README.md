# Academic Project Page Starter

This workspace now contains a ready-to-edit academic project page similar to common CV/AI paper websites.

## Current Structure

- `index.html`: Main page content (title, authors, abstract, video, method, results, citation).
- `src/styles.css`: Visual style and responsive layout.
- `src/main.js`: Small interaction for copying BibTeX.
- `img/`: Put teaser, method figure, and result images here.
- `video/`: Put local demo videos here.

## Quick Start (No Web Experience Needed)

1. Edit `index.html` and replace:
	- Project title
	- Author names and affiliations
	- Button links (`Paper`, `Code`, `Dataset`)
	- Abstract text
	- BibTeX block
2. Add your assets:
	- `img/teaser.png`
	- `img/method.png`
	- `img/result_01.png`, `img/result_02.png`, `img/result_03.png`
	- `video/demo.mp4`
3. Optional: replace the YouTube iframe link in `index.html` with your own video URL.

## Local Preview

Open `index.html` directly in your browser for a quick preview.

For a cleaner local server preview (recommended), run one of these commands in the project root:

```powershell
# If Python is installed
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploy on GitHub Pages

1. Create a GitHub repository and push this folder.
2. In repository Settings -> Pages:
	- Source: `Deploy from a branch`
	- Branch: `main` (or `master`), folder: `/ (root)`
3. Wait 1-3 minutes, then open:
	- `https://<your-username>.github.io/<repo-name>/`

## Notes

- The page is mobile-responsive by default.
- Missing images/videos will show as broken placeholders until you upload your own files.
- You can keep everything as static files; no backend is required.
