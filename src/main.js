const copyBtn = document.getElementById("copyBibBtn");
const bib = document.getElementById("bibtex");

if (copyBtn && bib) {
  copyBtn.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(bib.textContent || "");
      copyBtn.textContent = "Copied";
      setTimeout(() => {
        copyBtn.textContent = "Copy BibTeX";
      }, 1200);
    } catch (error) {
      copyBtn.textContent = "Copy failed";
      setTimeout(() => {
        copyBtn.textContent = "Copy BibTeX";
      }, 1200);
    }
  });
}
