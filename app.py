import streamlit as st
import io

def check_python_syntax(code, filename="<uploaded_script>"):
    """
    Checks the syntax of a given Python code string using compile().

    Args:
        code (str): The Python code to check.
        filename (str): The name of the file for error reporting.

    Returns:
        tuple: A tuple containing (is_valid, message).
               is_valid (bool): True if syntax is correct, False otherwise.
               message (str): A success or error message.
    """
    try:
        # The compile() function is the core of this tool.
        # - source: The code string to compile.
        # - filename: The name of the file the code came from (for error messages).
        # - mode: 'exec' is used for compiling a sequence of statements.
        compile(code, filename, 'exec')
        return True, "Success! The Python syntax is valid."
    except SyntaxError as e:
        # If compile() finds a syntax error, it raises a SyntaxError.
        # We catch it and format a user-friendly error message.
        error_message = f"Syntax Error at line {e.lineno}: {e.msg}"
        return False, error_message
    except Exception as e:
        # Catch other potential compilation errors, though SyntaxError is the most common.
        return False, f"An unexpected error occurred: {e}"

# --- Streamlit User Interface ---

# Set the title and a nice icon for the browser tab
st.set_page_config(page_title="Python Syntax Checker", page_icon="✅")

# Main title of the web app
st.title("🐍 Python Syntax Checker Tool")

# Project description
st.markdown("""
This tool helps you quickly check a Python script (`.py` file) for syntax errors without executing the code. 
It's perfect for beginners who want to validate their code before running it.

**How to use:**
1.  Upload your Python (`.py`) file using the file uploader below.
2.  The tool will automatically display the content of the file.
3.  Click the **"Check Syntax"** button to validate the code.
4.  The result will be displayed as either a success or an error message.
""")

# File uploader widget
uploaded_file = st.file_uploader("Choose a Python file", type="py")

if uploaded_file is not None:
    # To read file as string:
    # 1. getvalue() reads the file content as bytes.
    # 2. decode("utf-8") converts the bytes to a string.
    code_content = uploaded_file.getvalue().decode("utf-8")

    # Display the uploaded code in a code block
    st.subheader("Your Uploaded Code:")
    st.code(code_content, language='python')

    # Create a button to trigger the syntax check
    if st.button("Check Syntax", type="primary"):
        # Call our checking function
        is_valid, message = check_python_syntax(code_content, uploaded_file.name)

        # Display the result
        if is_valid:
            st.success(message)
        else:
            st.error(message)

else:
    st.info("Please upload a `.py` file to begin.")

# Add a footer
st.markdown("---")
st.write("Project based on the idea of using the built-in `compile()` function for static code analysis.")