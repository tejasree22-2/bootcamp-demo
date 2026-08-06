# Git & GitHub Bootcamp — KIET Group of Institutions

Welcome! This repository is the hands-on exercise for the **Git & GitHub Bootcamp** at KIET Group of Institutions. If you are here, you are about to make your very first open-source-style contribution. Don't worry — every step is explained, and mistakes are totally okay. That's what the bootcamp is for!

---

## What Is This Exercise About?

Each participant adds their own **profile page** to a shared showcase — all living in the same repository. By the end of the session you will have practised the core Git & GitHub workflow that real software teams use every day:

```
Fork → Clone → Edit → Commit → Push → Pull Request
```

---

## How It Works

1. Each **participant** forks this repository to their own GitHub account.
2. They clone their fork, create their folder inside `participants/`, fill in `info.json`, and write their own `index.html`.
3. They push their changes and open a **Pull Request** back to this repository.
4. A bot **automatically validates** the `info.json` — if it has any errors, the PR is blocked and the bot comments with the exact error message.
5. If the JSON is valid, the PR is **automatically merged** — no manual review needed.
6. When ready, the instructor runs the **Update Participants Page** workflow from GitHub Actions to refresh the live showcase with all merged profiles.

---

## Automation

This repository uses GitHub Actions to handle everything automatically:

| What | How |
|---|---|
| **JSON validation** | Every PR is checked — invalid `info.json` is blocked with an error comment |
| **Auto-merge** | Valid PRs are merged automatically without any manual approval |
| **Showcase update** | Instructor manually triggers the workflow to update `index.html` and deploy the live site |

> PRs that touch files outside the `participants/` folder are blocked automatically.

---

## How to Participate

Ready to add your page? All the instructions are in **[CONTRIBUTING.md](CONTRIBUTING.md)**.

It will walk you through every step:
- Forking and cloning the repo
- Creating your folder and filling in `info.json`
- Writing your own `index.html` profile page
- Committing and pushing your changes
- Opening a Pull Request

> First time using Git? No problem. The guide is written for absolute beginners and explains each command as you go.

---

## Project Structure

```
bootcamp-demo/
├── index.html              # Main showcase page (updated by update.py)
├── update.py               # Script that reads all info.json files and updates index.html
├── TEMPLATE/               # Copy this folder to create your own page
│   ├── index.html          # Starter template — replace with your own content
│   └── info.json           # Fill in your roll number, name, and photo URL
├── participants/
│   └── rollno-name/        # Your folder, named as your roll number + your name
│       ├── index.html      # Your profile page (you write this)
│       └── info.json       # Your roll number, name, and photo URL
├── .github/workflows/
│   ├── auto-merge.yml      # Validates info.json and auto-merges valid PRs
│   └── update-and-deploy.yml  # Manually triggered — updates index.html and deploys
├── CONTRIBUTING.md         # Step-by-step guide for contributors
└── README.md               # You are here!
```

---

## Need Help?

- Read through [CONTRIBUTING.md](CONTRIBUTING.md) carefully — it covers the most common questions.
- If you are still stuck, open an **Issue** on this repository and describe what went wrong. No question is too basic!
- Ask your bootcamp instructor.

---

*Happy committing! You've got this.*
