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

        
# Save the output to a text file
    with open("my_results.txt", "w") as f:
        f.write(f"--- VIT GRADE REPORT ---\n")
        f.write(f"Total Score: {user_total:.2f}\n")
        f.write(f"Predicted Grade: {grade}\n")
    
    print("\n[SUCCESS] Your report has been saved to 'my_results.txt'")

if __name__ == "__main__":
    calculate_advanced_relative()

