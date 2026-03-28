# # VIT Grade Guard - Full Semester Version
# # Includes Internals + Term End Exam (FAT)

# def calculate_final_grade():
#     print("--- VIT Bhopal Grade Guard (Full Report) ---")
    
#     # 1. Internal Inputs
#     mid_term = float(input("Mid Term (out of 50): "))
#     assignment = float(input("Assignment (out of 10): "))
#     group_act = float(input("Group Activity (out of 5): "))
#     quiz = float(input("Quiz (out of 10): "))
#     tutorial = float(input("Tutorial (out of 5): "))
#     attendance = float(input("Attendance (out of 5): "))

#     # 2. Term End Input (The New Part!)
#     tee_marks = float(input("Term End Exam / TEE (out of 100): "))

#     # 3. Weightage Math
#     w_midterm = (mid_term / 50) * 30
#     w_internal = assignment + group_act + quiz + tutorial + attendance
#     w_tee = (tee_marks / 100) * 30  # TEE is 30% weightage
    
#     final_score = w_midterm + w_internal + w_tee

#     print(f"\n--- YOUR FINAL REPORT ---")
#     print(f"Internal Weightage (70%): {w_midterm + w_internal:.2f}")
#     print(f"TEE Weightage (30%):      {w_tee:.2f}")
#     print(f"TOTAL SCORE:              {final_score:.2f} / 100")
#     print("-" * 30)

#     # 4. Grade Logic (VIT Standard Cutoffs)
#     if final_score >= 90:
#         grade = "S (Outstanding)"
#     elif final_score >= 80:
#         grade = "A (Excellent)"
#     elif final_score >= 70:
#         grade = "B (Very Good)"
#     elif final_score >= 60:
#         grade = "C (Good)"
#     elif final_score >= 50:
#         grade = "D (Fair)"
#     elif final_score >= 40:
#         grade = "E (Pass)"
#     else:
#         grade = "F (Fail - Needs Re-exam)"

#     print(f"PROBABLE GRADE: {grade}")

# if __name__ == "__main__":
#     calculate_final_grade()

#     # 2. Class Statistics (The "Relative" Part)
#     class_avg = float(input("\nEnter the estimated Class Average (out of 100): "))

#     # 3. Weightage Calculation
#     w_midterm = (mid_term / 50) * 30
#     w_internal = assignment + group_act + quiz + tutorial + attendance
#     w_tee = (tee_marks / 100) * 30
#     user_total = w_midterm + w_internal + w_tee

#     print(f"\n--- RELATIVE ANALYSIS ---")
#     print(f"Your Total: {user_total:.2f} | Class Avg: {class_avg:.2f}")

#     # 4. Relative Grading Logic (Standard VIT Deviation Logic)
#     # Usually: S is Avg + 15-20, A is Avg + 5-10
#     diff = user_total - class_avg

#     if diff >= 20:
#         rel_grade = "S (Top of the Class!)"
#     elif diff >= 10:
#         rel_grade = "A (Excellent Performance)"
#     elif diff >= 0:
#         rel_grade = "B (Above Average)"
#     elif diff >= -10:
#         rel_grade = "C (Average)"
#     elif diff >= -20:
#         rel_grade = "D (Below Average)"
#     else:
#         rel_grade = "E/F (Risk Zone)"

#     print(f"ESTIMATED RELATIVE GRADE: {rel_grade}")

# if __name__ == "__main__":
#     calculate_relative_grade()

# VIT Grade Guard - Dual-Average Edition
# This script compares your marks to the class average for both Mid-Term and FAT.

def calculate_advanced_relative():
    print("--- VIT Bhopal Grade Guard (Dual-Average Mode) ---")
    
    # 1. Your Marks
    mid_term = float(input("Your Mid-Term Marks (out of 50): "))
    tee_marks = float(input("Your Term End Exam Marks (out of 100): "))
    # Internals (Assignment, Quiz, etc. - usually have high averages, we'll sum them)
    internals = float(input("Sum of all other internals (out of 40): "))

    # 2. Class Averages (The "Relative" Data)
    avg_mid = float(input("Class Average for Mid-Term (out of 50): "))
    avg_tee = float(input("Class Average for Term End Exam (out of 100): "))

    # 3. Weightage Calculation
    # Your Total
    user_total = (mid_term/50)*30 + internals + (tee_marks/100)*30
    # Class Total (Approximated)
    class_total = (avg_mid/50)*30 + internals + (avg_tee/100)*30

    print(f"\n--- PERFORMANCE ANALYSIS ---")
    print(f"Your Total: {user_total:.2f} / 100")
    print(f"Class Total: {class_total:.2f} / 100")

    # 4. Relative Difference
    diff = user_total - class_total

    if diff >= 20:
        grade = "S (Top Tier)"
    elif diff >= 10:
        grade = "A (Above Average)"
    elif diff >= 0:
        grade = "B (On Average)"
    elif diff >= -10:
        grade = "C (Below Average)"
    else:
        grade = "D/E (Improvement Needed)"

    print(f"PREDICTED RELATIVE GRADE: {grade}")
    
    if mid_term < avg_mid and tee_marks > avg_tee:
        print("\nNote: Great comeback! You performed better in Term End Exam than Mid-Term.")
    elif mid_term > avg_mid and tee_marks < avg_tee:
        print("\nNote: Your Term End Exam score dropped below average. Watch out for the curve!")

if __name__ == "__main__":
    calculate_advanced_relative()