import streamlit as st
import subprocess
import os
import tempfile

st.title("💻 Run Shell Script in Streamlit")

# Upload .sh file
uploaded_file = st.file_uploader("Upload your shell script (.sh)", type=["sh"])

if uploaded_file is not None:
    # Save uploaded file to a temporary path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".sh") as tmp_file:
        tmp_file.write(uploaded_file.read())
        script_path = tmp_file.name

    st.success(f"Uploaded script: {uploaded_file.name}")

    # Run script on button click
    if st.button("▶ Run Script"):
        try:
            # Make it executable
            os.chmod(script_path, 0o755)

            # Run the script
            result = subprocess.run(
                ["bash", script_path],
                capture_output=True,
                text=True,
            )

            st.subheader("📜 Script Output:")
            if result.stdout:
                st.code(result.stdout)

            if result.stderr:
                st.error(result.stderr)

            # Allow download of logs
            log_content = f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
            st.download_button(
                label="📥 Download Logs",
                data=log_content,
                file_name="script_output.txt",
                mime="text/plain",
            )

        except Exception as e:
            st.error(f"Error: {e}")
