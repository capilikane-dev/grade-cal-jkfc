import streamlit as st

st.set_page_config(page_title="Grade Calculator", page_icon="📘")

st.title("📘 Student Grade Calculator")

# --- Inputs ---
absences = st.number_input("Absences", min_value=0, step=1)
prelim_exam = st.number_input("Prelim Exam (0-100)", 0.0, 100.0)
quizzes = st.number_input("Quizzes (0-100)", 0.0, 100.0)
requirements = st.number_input("Requirements (0-100)", 0.0, 100.0)
recitation = st.number_input("Recitation (0-100)", 0.0, 100.0)

if st.button("Compute Grade"):
    # --- Absence rule ---
    if absences >= 4:
        st.error("❌ FAILED due to 4 or more absences.")
    else:
        # --- Attendance ---
        attendance = max(0, 100 - (absences * 10))

        # --- Class standing ---
        class_standing = (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)

        # --- Prelim grade ---
        prelim_grade = (0.6 * prelim_exam) + (0.1 * attendance) + (0.3 * class_standing)

        st.success(f"Prelim Grade: {prelim_grade:.2f}")

        # --- Calculation function ---
        def required_grades(target, prelim):
            prelim_contrib = 0.2 * prelim
            needed = target - prelim_contrib

            equal = needed / 0.8
            equal = f"{equal:.2f}" if 0 <= equal <= 100 else "Not possible"

            mid_final100 = (needed - 0.5*100) / 0.3
            mid_final100 = f"{mid_final100:.2f}" if 0 <= mid_final100 <= 100 else "Not possible"

            final_mid100 = (needed - 0.3*100) / 0.5
            final_mid100 = f"{final_mid100:.2f}" if 0 <= final_mid100 <= 100 else "Not possible"

            return equal, mid_final100, final_mid100

        # --- Show results ---
        st.info("📊 Required Midterm & Final Grades:")

        for target, label in [(75, "Passing (75%)"), (90, "Dean’s Lister (90%)")]:
            eq, mid100, fin100 = required_grades(target, prelim_grade)
            st.write(f"**{label}:**")
            st.write(f"- Midterm = Finals → {eq}")
            st.write(f"- Finals = 100 → Midterm: {mid100}")
            st.write(f"- Midterm = 100 → Finals: {fin100}")
            st.divider()
