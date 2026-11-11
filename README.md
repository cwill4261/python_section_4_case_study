# Stephen Curry Sports Analytics

## Murach’s Python for Data Science — Chapter 15

Explore how Python can turn Stephen Curry’s shot records into season summaries and shot-location charts.

This lesson covers:

- Loading JSON data into a pandas DataFrame
- Cleaning data and converting dates
- Creating season labels and calculating field-goal points
- Summarizing data with `groupby()`
- Creating charts with Matplotlib
- Filtering three-point attempts and calculating shooting percentage

## Prerequisites

Before beginning, install:

- **Python 3.12**, the version used to test this project
- **Visual Studio Code**
- The **Python extension published by Microsoft** in VS Code
- **Git**, if cloning the repository

Internet access is needed to download the project and install packages. Jupyter is not required. The dataset is included in `data/shots.json`.

## 1. Access the Repository from Canvas

1. Open our course in Canvas.
2. Go to the discussion board containing my lesson post.
3. Click the GitHub repository link:

   [Stephen Curry Sports Analytics](https://github.com/cwill4261/python_section_4_case_study)

## 2. Download and Open the Project

### Recommended: Clone Using VS Code

1. Create a folder on your Desktop named **Python Class Projects**.
2. Open VS Code.
3. Open the Command Palette:
   - **Windows:** `Ctrl + Shift + P`
   - **macOS:** `Cmd + Shift + P`
4. Search for and select **Git: Clone**.
5. Paste this repository URL:

   ```text
   https://github.com/cwill4261/python_section_4_case_study.git
   ```

6. Choose **Desktop → Python Class Projects** as the destination. VS Code will create a `python_section_4_case_study` folder inside it.
7. When cloning finishes, select **Open**.

### Alternative: Download a ZIP

If Git is unavailable:

1. On the GitHub repository page, select **Code → Download ZIP**.
2. Extract the ZIP into **Desktop → Python Class Projects**.
3. In VS Code, select **File → Open Folder**.
4. Open the extracted folder containing `README.md` and `requirements.txt`.

Extract the ZIP before running the code.

## 3. Install the Required Packages

In VS Code, select **Terminal → New Terminal**.

Make sure the terminal is in the project folder containing `requirements.txt`. Run the commands for your operating system one at a time.

### Windows

Create a virtual environment:

```powershell
py -3.12 -m venv .venv
```

Install the packages:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### macOS or Linux

With Python 3.12 installed, create a virtual environment:

```bash
python3.12 -m venv .venv
```

Install the packages:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

The virtual environment keeps this project’s packages separate from other Python projects. These commands use it directly, so activation is not necessary.

A notice about a newer version of pip does not require action.

The Windows instructions have been tested by the author. The macOS/Linux instructions have not yet been independently tested.

## 4. Select the Python Environment in VS Code

1. Open `code/lesson_examples.py`.
2. Open the Command Palette.
3. Select **Python: Select Interpreter**.
4. Choose the environment containing **`.venv`**.

If it is not listed, choose **Enter interpreter path** and browse to:

- **Windows:** `.venv/Scripts/python.exe`
- **macOS/Linux:** `.venv/bin/python`

## 5. Run the Lesson

From the project’s terminal, run:

### Windows

```powershell
.\.venv\Scripts\python.exe code/lesson_examples.py
```

### macOS or Linux

```bash
.venv/bin/python code/lesson_examples.py
```

The script prints:

- A preview of the shot records
- Original and cleaned shot counts
- Season shooting summaries

It also displays two chart windows in sequence. **Close the first chart window to continue to the second.**

Charts are saved automatically:

- `outputs/season_scoring.png`
- `outputs/shot_locations.png`

The shot-location chart displays the half-court area. Attempts outside its plotting limits are not shown, although the panel titles count all regulation-time attempts in each selected season.

## 6. Complete the Class Practice

Open `code/practice_tasks.py` and complete the comments labeled **TODO**:

1. Choose a season from `2009-2010` through `2018-2019`.
2. Filter the selected season to three-point attempts.
3. Calculate shooting percentage: **makes ÷ attempts × 100**.

For our shared answer check, use `2015-2016`. Afterward, try another season.

### Run on Windows

```powershell
.\.venv\Scripts\python.exe code/practice_tasks.py
```

### Run on macOS or Linux

```bash
.venv/bin/python code/practice_tasks.py
```

Before TODO 2 is completed, the starter counts all field-goal attempts, not just three-pointers. Different counts between the unfinished starter and the solution are expected.

## 7. Check Your Answer

After attempting the exercise, review `code/practice_solutions.py`.

### Run on Windows

```powershell
.\.venv\Scripts\python.exe code/practice_solutions.py
```

### Run on macOS or Linux

```bash
.venv/bin/python code/practice_solutions.py
```

For `2015-2016`, the completed exercise produces:

- **875** regulation-time three-point attempts
- **398** made three-pointers
- **45.49%** three-point shooting accuracy

## Troubleshooting

### Python command is not recognized

Confirm that Python 3.12 is installed, then close and reopen VS Code.

On Windows, check with:

```powershell
py -3.12 --version
```

On macOS/Linux, check with:

```bash
python3.12 --version
```

### `No module named 'pandas'` or `'matplotlib'`

Install the requirements using the commands in Step 3, then run the scripts using the explicit `.venv` commands in Step 5.

### Python cannot find the script or requirements file

Make sure the terminal is in the project’s main folder and that the filenames match the commands exactly.

### The dataset cannot be found

Confirm that `shots.json` is inside the project’s `data` folder. No separate dataset download is needed.

### Only one chart appears

Close the first chart window. The script will then display the second chart.

## Interpretation and Limitations

This analysis excludes overtime and free throws. Field-goal points per game are therefore not the same as total points per game.

Games counted in the summary are games with recorded regulation-time shot attempts in this dataset. Season labels follow the textbook’s July cutoff.

Shot-location plots show individual attempts. A more crowded plot does not automatically indicate better shooting accuracy.

## Source and Acknowledgment

Adapted for a classroom lesson from Chapter 15 of *Murach’s Python for Data Science* and its accompanying sports analytics notebook.

Dataset source: [Murach’s shot data](https://www.murach.com/python_analysis/shots.json).

The simplified basketball court illustration was created using Matplotlib shapes.