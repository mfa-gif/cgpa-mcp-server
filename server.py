import os
from fastmcp import FastMCP
import tools

mcp = FastMCP("cgpa")

mcp.tool(tools.marks_to_grade_points)
mcp.tool(tools.calculate_semester_gpa)
mcp.tool(tools.calculate_new_cgpa)
mcp.tool(tools.required_gpa_for_target)
mcp.tool(tools.get_semester_courses)
mcp.tool(tools.get_remaining_credit_hours)
mcp.tool(tools.get_credit_hours)
mcp.tool(tools.save_report)

if __name__ == "__main__":
    # Locally: http://127.0.0.1:8000/mcp
    # On hosting: the host sets the PORT variable
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "127.0.0.1")
    mcp.run(transport="http", host=host, port=port)
