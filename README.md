# NeetCode Problem Parser and Generator
This tool is designed to enhance your problem-solving experience on `neetcode.io` by giving you more control over how you select problems to solve.

![demo-ezgif com-speed](https://github.com/user-attachments/assets/f5179b3b-97f8-4716-b006-8adb4cefaff6)

## What It Does
This repo allows you to filter Neetcode problems based on category and difficulty, helping you practice more effectively.

First, you need to scrape the `neetcode.io` problems using BeautifulSoup. Then, run the `neetcode_parser.py` script. This script processes the HTML, extracting problem information and storing it in a `parsed_neatcode.csv` file. The CSV file includes key details like problem category, difficulty, and completion status Use the `get_problem.py` script to filter problems by category and difficulty. This script allows you to focus on the types of problems you want to practice, avoiding those that are too easy or too hard.

## Setup Instructions
### Step 0. Clone this Repo
Clone this repository with

```bash
git clone https://github.com/al3xisrobles/NeetCode-Problem-Parser-and-Generator.git
```

### Step 1. Scrape neetcode.io
1. Go to `neetcode.io` and login. Navigate to the Practice tab, then the Neetcode All tab within it.
2. Switch to the "Grouped View" where all problem categories are listed.
3. Expand all categories, starting from the bottom (e.g., JavaScript) and working your way up to the top (e.g., Arrays & Hashing).
4. Right-click anywhere on the page and select Inspect (or use the hotkey: Cmd + Option + I on Mac or Ctrl + Shift + I on Windows/Linux).
5. In the Elements tab that appears, find the `<html>` tag at the top of the DOM tree.
6. Right-click the `<html>` tag, select Copy > Copy outerHTML.
7. Paste this HTML into a new file called `neetcode.html` in your cloned repo at the root directory.

### Step 2: Parse the HTML
Start a virtual environment and install all of this project's dependencies with the command:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the following command to parse the copied HTML and generate the CSV file:

```bash
python neetcode_parser.py
```

This will create a `parsed_neatcode.csv` file with all the problems, their categories, difficulties, and completion statuses.

### Step 3: Get Your Filtered Problems
Run the following command to filter problems by category and difficulty:

```bash
python get_problem.py
```

The script will prompt you for the category and difficulty level you're interested in, then return a problem that matches your criteria. After solving the problem, press Enter to update the CSV file with your completion status, as well as receive a new problem.

Happy coding! 🚀
