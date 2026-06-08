# Host portfolio.ealu.ai on Spaceship

This guide covers publishing the static site in this repo to **portfolio.ealu.ai** using Spaceship.

You have two good options. Pick based on how you want to update the site.

| Option | Best if you want… | Updates via |
| --- | --- | --- |
| **A. Shared hosting** | Simplest setup, lowest cost for a static page | Upload files (or FTP) |
| **B. Deploy from GitHub** | Push to GitHub → site updates automatically | Git push |

Both work with a subdomain like `portfolio.ealu.ai` when **ealu.ai** is on Spaceship.

---

## Prerequisites

- A Spaceship account: https://www.spaceship.com
- Domain **ealu.ai** registered or managed in Spaceship (or DNS you can edit)
- This project pushed to a GitHub repository (for Option B)

---

## Option A — Shared hosting (simplest)

Best for a static HTML site with occasional manual updates.

### Step 1: Add web hosting in Spaceship

1. Log in to Spaceship.
2. Open **Launchpad** (your account dashboard).
3. Add **Web Hosting** if you do not already have a plan.
   - Product page: https://www.spaceship.com/web-hosting/
4. Complete checkout / activation.

### Step 2: Connect the subdomain

1. Open **Hosting Manager** from Launchpad.
2. Add a website for **portfolio.ealu.ai** (or add it as a subdomain under **ealu.ai**).
3. Note the document root folder for this site (often something like `public_html/portfolio` or a subdomain folder).

### Step 3: Upload your site files

Upload these files from this repo into that folder:

- `index.html`
- `styles.css`
- `script.js`
- `resume.pdf` (your real PDF)

Ways to upload:

- **File Manager** in Hosting Manager, or
- **FTP/SFTP** credentials from Hosting Manager

Your folder should look like:

```text
index.html
styles.css
script.js
resume.pdf
```

There is no build step. The site is ready once those files are live.

### Step 4: Point DNS for portfolio.ealu.ai

If **ealu.ai** is on Spaceship:

1. Open **Domain Manager** → select **ealu.ai**.
2. Open **Advanced DNS**.
3. Add or edit a record for the subdomain:

   | Type | Host / Name | Value |
   | --- | --- | --- |
   | **A** or **CNAME** | `portfolio` | Use the target Spaceship shows in Hosting Manager |

Spaceship often provides the exact record when you attach the domain to hosting—follow what Hosting Manager recommends.

### Step 5: Enable SSL

1. In Hosting Manager, open SSL for **portfolio.ealu.ai**.
2. Enable the free SSL certificate (included with Spaceship hosting).
3. Wait a few minutes for issuance, then open https://portfolio.ealu.ai

### Step 6: Verify

- Homepage loads with all sections
- Resume download works
- Navigation links scroll to each section
- Site looks correct on mobile

---

## Option B — Deploy from GitHub (auto-updates on push)

Spaceship’s **Starlight Hyperlift** product deploys apps from GitHub. For a static site, it runs your files in a small web server container. You do not need to understand containers—just add the included `Dockerfile` and connect the repo.

Product info: https://www.spaceship.com/starlight-cloud/hyperlift/

### Step 1: Push this repo to GitHub

```bash
cd /path/to/ealu-portfolio
git add .
git commit -m "Add TPM portfolio site"
git remote add origin git@github.com:YOUR_USERNAME/ealu-portfolio.git
git push -u origin main
```

Replace `YOUR_USERNAME` and repo name with yours.

### Step 2: Connect GitHub to Hyperlift

1. In Spaceship Launchpad, open **Starlight Hyperlift** (Hyperlift Manager).
2. Choose **Connect GitHub** and authorize the Spaceship GitHub app.
3. Select **only** the repository for this portfolio (recommended for security).
4. Choose branch: **main**.

### Step 3: Configure the app

In the Hyperlift setup panel:

| Setting | Value |
| --- | --- |
| **Dockerfile path** | `Dockerfile` |
| **Port** | Set via Hyperlift env var if prompted: `8080` |
| **Automatic builds** | **On** (redeploy when you push to GitHub) |

Click **Build**, then wait for build and deploy to finish.

Hyperlift assigns a temporary URL (e.g. `your-app.hyperlift.spaceship.com`). Confirm the site loads there first.

### Step 4: Attach custom domain portfolio.ealu.ai

1. In Hyperlift Manager → your app → **Domains** (or custom domain settings).
2. Add **portfolio.ealu.ai**.
3. Spaceship will show DNS instructions. Typically you add:

   | Type | Host | Value |
   | --- | --- | --- |
   | **CNAME** | `portfolio` | Target shown by Hyperlift |

4. SSL is usually provisioned automatically after DNS propagates (often 5–30 minutes, sometimes longer).

### Step 5: Verify and iterate

1. Open https://portfolio.ealu.ai
2. Change content locally → commit → push → Hyperlift rebuilds automatically (if automatic builds are on)

---

## Which option should you use?

- **Most people with a simple portfolio:** Option A (shared hosting).
- **You want GitHub as source of truth and auto-deploy:** Option B (Hyperlift + GitHub).

You do not need both. Use one.

---

## Troubleshooting

### Site shows “Not found” or default Spaceship page

- DNS may still be propagating. Wait up to 24 hours (usually much less).
- Confirm files are in the correct hosting folder (Option A) or the Hyperlift build succeeded (Option B).

### Resume link does not download

- Ensure `resume.pdf` is uploaded / committed and is a real PDF, not the placeholder text file.

### CSS or JS missing

- All files must sit in the same directory as `index.html` (Option A) or be copied in the `Dockerfile` (Option B—already configured in this repo).

### Mixed content / not secure

- Force HTTPS in Hosting Manager or wait for Hyperlift SSL to finish provisioning.

---

## Quick checklist before sharing with recruiters

- [ ] Real name, email, and LinkedIn in Contact section
- [ ] Resume PDF uploaded
- [ ] https://portfolio.ealu.ai loads on desktop and phone
- [ ] No placeholder “Company Name” or “20XX” left if you want a polished public site

---

## Support links

- Spaceship Web Hosting: https://www.spaceship.com/web-hosting/
- Hyperlift: https://www.spaceship.com/starlight-cloud/hyperlift/
- Hyperlift + GitHub + Dockerfile guide: https://www.spaceship.com/knowledgebase/hyperlift-deploy-app-github-dockerfile/
