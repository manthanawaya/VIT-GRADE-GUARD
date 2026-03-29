# 🛡️ VIT-Bhopal Grade Guard (Relative Analytics Edition)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-VITyarthi-orange)

## 📖 Project Overview
**Grade Guard** is a specialized Python analytics tool developed for students at **VIT Bhopal**. Navigating the **Relative Grading** system can be stressful; this tool eliminates the guesswork by providing a data-driven prediction of final grades based on real-time class performance.

Unlike a standard GPA calculator, Grade Guard implements **Dual-Average Logic**, comparing individual scores against fluctuating class means for both Mid-Term and Term-End  examinations.

---
Problem Statement
At VIT, many courses use relative grading, where your final grade depends not only on your marks but also on the distribution of marks in the class. Students often:
1.Do not know how each component (MTE, TEE, assignments, quizzes, labs) contributes to the final grade.
2.Struggle to understand how much they must score in upcoming evaluations to reach a target grade.
3.Feel anxious because they cannot easily estimate their relative position in the course.

VIT GRADE GUARD addresses this by providing a simple, offline, terminal-based tool that:

1.Combines all evaluation components using real weightages.
2.Simulates relative grading using class statistics.
3.Gives clear feedback on current performance and possible grade outcomes.


## ✨ Key Features
* **Official Weightage Integration:** Hard-coded to match the 2026 assessment breakdown (30% Midterm, 40% Internals, 30% TEE).
* **Relative Grading Simulation:** Predicts S, A, and B grades by calculating the "Z-Gap" between the user and the class average.
* **Dual-Stage Tracking:** Handles different max marks for Mid-Term (50) and TEE (100) seamlessly.
* **Performance Insights:** Provides automated feedback on whether your performance is "Above the Curve" or in the "Risk Zone."
* **Data Persistence:** Automatically saves your final report to a local `.txt` file for future reference.

---

## 🛠️ Technical Implementation
### The Logic Flow
The project follows a modular functional approach:
1.  **Input Module:** Captures Mid-term, Quiz, Assignment, Tutorial, and Attendance marks.
2.  **Normalization Engine:** Converts raw marks into weighted percentages out of 100.
3.  **Statistical Comparison:** Subtracts the User Total from the Class Average Total to determine the relative standing.
4.  **Reporting:** Generates a summary and writes a permanent log file.



---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher installed on your machine.
* A terminal or command prompt.

### Installation & Usage
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/manthanawaya/VIT-GRADE-GUARD.git](https://github.com/manthanawaya/VIT-GRADE-GUARD.git)
    ```
2.  **Navigate to the Directory:**
    ```bash
    cd VIT-GRADE-GUARD
    ```
3.  **Run the Application:**
    ```bash
    python GRADE-GUARD.py
    ```

---

## 📁 Project Structure
```text
VIT-GRADE-GUARD/
├── GRADE-GUARD.py     # Main application logic
├── README.md          # Project documentation (this file)
├── my_results.txt     # Auto-generated report file
└── .gitignore         # Files to be ignored by Git
