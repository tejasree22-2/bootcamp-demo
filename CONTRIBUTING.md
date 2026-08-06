# How to Add Your Page — Step-by-Step Guide

Welcome! Follow these steps to add your own profile page to the bootcamp showcase.
This guide is written for beginners, so every step is explained in detail.

---

## What You Will Need

- A [GitHub account](https://github.com) (free)
- [Git](https://git-scm.com/downloads) installed on your computer
- A text editor (e.g. [VS Code](https://code.visualstudio.com/))

---

## Step 1 — Fork this Repository

A **fork** is your own personal copy of this project on GitHub.

1. Go to the top of this repository's GitHub page.
2. Click the **Fork** button (top-right corner).
3. GitHub will create a copy of the repo under your account.

---

## Step 2 — Clone Your Fork to Your Computer

**Cloning** downloads your fork so you can edit files locally.

1. On your forked repo page, click the green **Code** button.
2. Copy the URL shown (it will look like `https://github.com/YOUR-USERNAME/bootcamp-demo.git`).
3. Open a terminal (Command Prompt, Git Bash, or Terminal) and run:

```bash
git clone https://github.com/YOUR-USERNAME/bootcamp-demo.git
```

4. Move into the project folder:

```bash
cd bootcamp-demo
```

---

## Step 3 — Create Your Folder

Inside the `participants/` folder, create a new folder named using your **roll number and name**:

```
rollno-yourname
```

**Examples:** `21BCE001-ravi`, `21BCE002-sneha`, `21BCE003-priya`

**On Mac / Linux:**

```bash
mkdir participants/21BCE001-yourname
```

**On Windows (Command Prompt):**

```cmd
mkdir participants\21BCE001-yourname
```

> Use your actual roll number and your first name (or GitHub username). Keep it lowercase with no spaces.

---

## Step 4 — Fill in info.json

Copy the `info.json` from the `TEMPLATE/` folder into your new folder:

**On Mac / Linux:**

```bash
cp TEMPLATE/info.json participants/21BCE001-yourname/info.json
```

**On Windows:**

```cmd
copy TEMPLATE\info.json participants\21BCE001-yourname\info.json
```

Open `info.json` in your text editor and fill in your details:

```json
{
  "roll_no": "21BCE001",
  "name": "Your Full Name",
  "photo": "https://github.com/your-github-username.png"
}
```

- `roll_no` — your college roll number
- `name` — your full name as you want it shown on the main page
- `photo` — your GitHub profile picture URL (replace `your-github-username` with your actual GitHub username)

Save the file when you are done.

---

## Step 5 — Write Your index.html

Copy the starter template into your folder:

**On Mac / Linux:**

```bash
cp TEMPLATE/index.html participants/21BCE001-yourname/index.html
```

**On Windows:**

```cmd
copy TEMPLATE\index.html participants\21BCE001-yourname\index.html
```

Open `participants/21BCE001-yourname/index.html` in your text editor and replace all the placeholder text with your real information. Look for the `✏️` comments — they mark every spot you need to update:

- Your role or track (Frontend, Data Science, etc.)
- Your city and country
- Your email and GitHub link
- A short introduction about yourself
- Your project title and description
- Your skills
- What you built or learned
- A fun fact about yourself

Save the file when you are done.

---

## Step 6 — Commit and Push Your Changes

Now save your changes to Git and upload them to GitHub.

```bash
# Stage your new folder
git add participants/21BCE001-yourname/

# Create a commit with a clear message
git commit -m "Add 21BCE001-yourname"

# Push to your fork on GitHub
git push origin main
```

> Replace `21BCE001-yourname` with your actual folder name.

---

## Step 7 — Create a Pull Request

A **pull request** (PR) asks the maintainers to add your changes to the main project.

1. Go to your forked repo on GitHub.
2. You should see a banner saying **"Compare & pull request"** — click it.
   - If you don't see it, click the **Pull requests** tab, then **New pull request**.
3. Make sure:
   - **base repository** is the original `bootcamp-demo` repo
   - **head repository** is your fork
4. Give your PR a short title, e.g. `Add 21BCE001-yourname`.
5. Click **Create pull request**.

That's it! Once your PR is merged, your profile card — with your photo, name, and roll number — will appear on the main showcase page.

---

## Important Rules to Avoid Errors

### Your info.json must be valid JSON

Before submitting your PR, double-check your `info.json`. A single missing quote, comma, or bracket will cause the merge to fail automatically.

Valid example:
```json
{
  "roll_no": "21BCE001",
  "name": "Your Full Name",
  "photo": "https://github.com/your-github-username.png"
}
```

Common mistakes:
- Missing `"` around a value
- Missing `,` between fields
- Extra `,` after the last field
- Using `'` single quotes instead of `"` double quotes

If your `info.json` has an error, the bot will automatically comment on your PR with the exact error. Fix the file and push again to the **same branch** — the PR will re-check and merge automatically.

### Do NOT open a second PR to fix a mistake

If your PR has an error, **do not close it and open a new one**. Instead:

1. Fix the mistake in your local file
2. Save it
3. Run:

```bash
git add participants/your-folder/info.json
git commit -m "fix info.json"
git push origin main
```

Your existing PR will update automatically and the merge will retry.

### Only add files inside your own folder

Your PR should only contain files inside `participants/your-folder/`. Touching any other file will cause the auto-merge to be blocked.

---

## Need Help?

If you get stuck at any step, open an **Issue** on this repository and describe what went wrong. We're happy to help!
