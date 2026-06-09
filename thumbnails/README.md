# LinkedIn featured link thumbnails

Original graphics for LinkedIn **Featured** link uploads (1200×627 PNG). No third-party logos or trademarked imagery—abstract icons and portfolio typography only.

| File | Use for |
|------|---------|
| `portfolio.png` | Main portfolio / homepage featured link |
| `case-apple.png` | `https://portfolio.ealu.ai/case-apple.html` |
| `case-ppp.png` | `https://portfolio.ealu.ai/case-ppp.html` |
| `case-fiserv.png` | `https://portfolio.ealu.ai/case-fiserv.html` |
| `case-vineti.png` | `https://portfolio.ealu.ai/case-vineti.html` |
| `case-ealu.png` | `https://portfolio.ealu.ai/case-ealu.html` |

## Regenerate

```bash
python3 scripts/generate-thumbnails.py
```

Requires [Pillow](https://pypi.org/project/pillow/) (`pip install pillow`).

After deploy, thumbnails are also referenced by Open Graph / Twitter meta tags on each HTML page for link previews when URLs are shared.
