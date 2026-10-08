# Contributing to This Project

Thank you for wanting to help! This project is a student project, and everyone is welcome to contribute, whether you are new to coding or have some experience. Please be kind and respectful to everyone.

You will need:
- Python installed on your computer
- Git installed on your computer
- A GitHub account

---

## 1. How to Report an Issue

Found a bug or a problem? Let us know by opening an issue.

1. Go to the **Issues** tab of the repository.
2. Click **New issue**.
3. Give it a short, clear title (for example: `Program crashes when input is empty`).
4. In the description, include:
   - **What happened:** what you saw
   - **What you expected:** what should have happened
   - **Steps to reproduce:** how someone else can see the same problem
   - **Error message:** copy and paste it, if there is one
   - **Your setup:** your Python version and operating system
5. Click **Submit new issue**.

Tip: Search existing issues first to check that no one has reported it already.

---

## 2. How to Suggest a Feature

Have an idea to make the project better? We would love to hear it.

1. Go to the **Issues** tab and click **New issue**.
2. Start the title with `Feature:` (for example: `Feature: Add a score history`).
3. In the description, explain:
   - **What** you would like to see added
   - **Why** it would be useful
   - **How** you think it could work (optional)
4. Submit the issue and wait for feedback before you start coding. This avoids wasted effort if the idea needs changes.

---

## 3. How to Create a Branch

Never work directly on the `main` branch. Create your own branch instead.

1. **Fork** the repository (click **Fork** on GitHub) if you are not a member of the project.
2. **Clone** your copy to your computer:
   ```
   git clone <your-repository-url>
   ```
3. Go into the project folder:
   ```
   cd <project-folder-name>
   ```
4. Create and switch to a new branch:
   ```
   git checkout -b your-branch-name
   ```

Use a short, descriptive branch name, such as `fix-empty-input-bug` or `add-score-history`.

---

## 4. How to Make Changes

1. Make your changes in the project files using any editor you like.
2. Keep each branch focused on **one** fix or feature.
3. Check what you changed:
   ```
   git status
   ```
4. Add your changes:
   ```
   git add .
   ```
5. Save them with a clear message:
   ```
   git commit -m "Fix crash when input is empty"
   ```

Good commit messages are short and say what you did, for example `Add function to calculate average`.

---

## 5. How to Test Changes

Before you share your work, make sure it runs correctly.

1. Run the program and try out the part you changed:
   ```
   python your_file.py
   ```
2. Try normal inputs, and also unusual ones (empty input, very large numbers, wrong types).
3. Make sure you did not break anything that worked before.
4. If the project includes tests, run them using the instructions in the project's README, and make sure they pass.
5. If you fixed a bug, confirm the original problem no longer happens.

---

## 6. How to Create a Pull Request

1. Push your branch to GitHub:
   ```
   git push origin your-branch-name
   ```
2. Open the repository on GitHub. You should see a button to **Compare & pull request**. Click it.
3. Write a clear title and description:
   - What did you change?
   - Why did you change it?
   - How did you test it?
4. If your pull request solves an issue, mention it (for example: `Fixes #12`).
5. Click **Create pull request**.
6. Wait for a review. If someone asks for changes, update your branch and push again. The pull request will update automatically.

Be patient and polite during reviews. Feedback is a normal part of learning.

---

## 7. Basic Coding Guidelines

- **Use clear names.** Prefer `student_count` over `x`.
- **Follow Python naming style.** Use `snake_case` for variables and functions, and `CamelCase` for classes.
- **Use 4 spaces** for indentation (not tabs).
- **Keep functions small.** Each function should do one thing.
- **Write comments** to explain *why* something is done, not just *what*.
- **Add a short docstring** to each function describing what it does.
- **Do not leave unused code** or old commented-out code in your changes.
- **Do not include secrets** such as passwords or personal information.
- **Keep lines reasonably short** (around 79 to 100 characters) so they are easy to read.

---

## Need Help?

If you are stuck or unsure about anything, open an issue and ask your question. There are no silly questions here. Happy coding!
