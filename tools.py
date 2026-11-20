

COURSES = {
    1: [
        ("MS-251", "Probability & Statistics", 3.0),
        ("GE-160", "Applications of ICT", 3.0),
        ("GE-169", "Applied Physics", 3.0),
        ("GE-167", "Discrete Structures", 3.0),
        ("HQ-001", "Quran Translation - I", 0.5),
        ("GE-190", "Functional English", 3.0),
    ],
    2: [
        ("CC-112", "Programming Fundamentals", 3.0),
        ("CC-112-L", "Programming Fundamentals Lab", 1.0),
        ("CC-110", "Digital Logic Design", 2.0),
        ("CC-110-L", "Digital Logic Design Lab", 1.0),
        ("MS-252", "Linear Algebra", 3.0),
        ("GE-191", "Expository Writing", 3.0),
        ("GE-163", "Islamic Studies", 2.0),
        ("HQ-002", "Quran Translation - II", 0.5),
    ],
    3: [
        ("CC-211", "Object Oriented Programming", 3.0),
        ("CC-211-L", "Object Oriented Programming Lab", 1.0),
        ("CC-215", "Database Systems", 3.0),
        ("CC-215-L", "Database Systems Lab", 1.0),
        ("CC-210", "Computer Organization & Assembly Language", 3.0),
        ("GE-162", "Calculus & Analytical Geometry", 3.0),
        ("GE-192", "Introduction to Management", 2.0),
        ("HQ-003", "Quran Translation - III", 0.5),
    ],
    4: [
        ("CC-213", "Data Structures", 3.0),
        ("CC-213-L", "Data Structures Lab", 1.0),
        ("CC-312", "Information Security", 3.0),
        ("CC-214", "Computer Networks", 3.0),
        ("CC-212", "Software Engineering", 3.0),
        ("DC-220", "Advanced Database Management Systems", 3.0),
        ("HQ-004", "Quran Translation - IV", 0.5),
    ],
    5: [
        ("CC-313", "Analysis of Algorithms", 3.0),
        ("CC-310", "Artificial Intelligence", 3.0),
        ("DC-320", "Theory of Automata and Formal Languages", 3.0),
        ("DC-321", "Human Computer Interaction", 3.0),
        ("DC-322", "Computer Architecture", 3.0),
        ("EC-330", "Web Technologies / Elective", 3.0),
        ("HQ-005", "Quran Translation - V", 0.5),
    ],
    6: [
        ("CC-311", "Operating Systems", 3.0),
        ("EC-333", "Mobile Application Development / Elective", 3.0),
        ("EC-324", "Software Construction & Development / Elective", 3.0),
        ("EC-335", "Machine Learning / Elective", 3.0),
        ("EC-334", "Game Design and Development / Elective", 3.0),
        ("MS-253", "Multivariable Calculus", 3.0),
        ("HQ-006", "Quran Translation - VI", 0.5),
    ],
    7: [
        ("CC-411", "Final Year Project - I", 2.0),
        ("DC-328", "Parallel & Distributed Computing", 3.0),
        ("EC-345", "Computer Vision / Elective", 3.0),
        ("EC-425", "Software Quality Engineering / Elective", 3.0),
        ("MS-254", "Technical and Business Writing", 3.0),
        ("GE-263", "Entrepreneurship", 2.0),
        ("GE-262", "Professional Practices", 2.0),
        ("HQ-007", "Quran Translation - VII", 0.5),
    ],
    8: [
        ("CC-412", "Final Year Project - II", 4.0),
        ("DC-421", "Compiler Construction", 3.0),
        ("UE-272", "Introduction to Marketing", 3.0),
        ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
        ("GE-363", "Civics and Community Engagement", 2.0),
        ("HQ-008", "Quran Translation - VIII", 0.5),
    ],
}


def marks_to_grade_points(marks: int) -> float | str:
    """Use this when the user gives marks and wants to know the corresponding grade point."""
    if marks < 0 or marks > 100:
        return "Error: marks must be between 0 and 100"

    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2.0
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0


def calculate_semester_gpa(
    grade_points: list[float],
    credit_hours: list[float]
) -> float | str:
    """Use this when the user provides grade points and credit hours and wants to know semester GPA."""
    if len(grade_points) != len(credit_hours):
        return "Error: grade points and credit hours must have the same length"

    if len(grade_points) == 0:
        return "Error: at least one course is required"

    if any(g < 0 or g > 4 for g in grade_points):
        return "Error: grade points must be between 0 and 4"

    if any(c <= 0 for c in credit_hours):
        return "Error: credit hours must be greater than 0"

    total_quality_points = sum(
        grade_points[i] * credit_hours[i]
        for i in range(len(grade_points))
    )

    total_credit_hours = sum(credit_hours)

    return round(total_quality_points / total_credit_hours, 2)


def calculate_new_cgpa(
    current_cgpa: float,
    completed_credit_hours: float,
    semester_gpa: float,
    semester_credit_hours: float
) -> float | str:
    """Use this when the user wants projected CGPA after adding one semester."""
    if current_cgpa < 0 or current_cgpa > 4:
        return "Error: current CGPA must be between 0 and 4"

    if semester_gpa < 0 or semester_gpa > 4:
        return "Error: semester GPA must be between 0 and 4"

    if completed_credit_hours <= 0 or semester_credit_hours <= 0:
        return "Error: credit hours must be greater than 0"

    new_cgpa = (
        current_cgpa * completed_credit_hours
        + semester_gpa * semester_credit_hours
    ) / (completed_credit_hours + semester_credit_hours)

    return round(new_cgpa, 2)


def required_gpa_for_target(
    target_cgpa: float,
    current_cgpa: float,
    completed_credit_hours: float,
    remaining_credit_hours: float
) -> float | str:
    """Use this when the user wants the GPA needed to reach a target CGPA."""
    if target_cgpa < 0 or target_cgpa > 4:
        return "Error: target CGPA must be between 0 and 4"

    if current_cgpa < 0 or current_cgpa > 4:
        return "Error: current CGPA must be between 0 and 4"

    if completed_credit_hours <= 0 or remaining_credit_hours <= 0:
        return "Error: credit hours must be greater than 0"

    required = (
        target_cgpa * (completed_credit_hours + remaining_credit_hours)
        - current_cgpa * completed_credit_hours
    ) / remaining_credit_hours

    return round(required, 2)


def get_semester_courses(semester: int) -> str:
    """Use this when the user asks which courses are offered in a semester."""
    if semester not in COURSES:
        return "Error: semester must be between 1 and 8"

    courses = COURSES[semester]

    result = []
    for code, name, credit_hours in courses:
        result.append(f"{code} - {name} ({credit_hours} CH)")

    return "\n".join(result)


def get_remaining_credit_hours(current_semester: int) -> float | str:
    """Use this when the user asks for the remaining credit hours from a given semester to graduation."""
    if current_semester not in COURSES:
        return "Error: semester must be between 1 and 8"

    total = 0.0

    for semester in range(current_semester, 9):
        for _, _, credit_hours in COURSES[semester]:
            total += credit_hours

    return round(total, 1)


def save_report(filename: str, content: str) -> str:
    """Use this only when the user has useful GPA information and explicitly asks to save a report."""
    if not filename:
        return "Error: filename cannot be empty"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        return f"Report saved successfully as {filename}"

    except Exception as error:
        return f"Error: could not save report - {error}"


def get_credit_hours(semesters: list[int]) -> float | str:
    """Use this to get the total credit hours of a list of semesters, for example [5, 6]."""
    total = 0.0
    for s in semesters:
        if s not in COURSES:
            return "Error: semester must be between 1 and 8"
        for code, name, credit_hours in COURSES[s]:
            total += credit_hours
    return round(total, 1)
