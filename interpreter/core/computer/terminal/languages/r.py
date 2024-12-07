"""R language support"""

import subprocess

from .subprocess_language import SubprocessLanguage


class R(SubprocessLanguage):
    """R programming language support"""

    file_extension = "r"
    name = "R"

    def __init__(self):
        super().__init__()
        self.start_cmd = ["Rscript", "--vanilla", "-"]

    def preprocess_code(self, code):
        """Add end of execution marker"""
        # Add commands that tell us what line is being executed
        processed_code = code
        # Add end command (we'll be listening for this so we know when it ends)
        processed_code += '\ncat("##end_of_execution##\\n")'
        return processed_code

    def line_postprocessor(self, line):
        """Process output lines"""
        return line

    def detect_active_line(self, line):
        """Detect active line markers"""
        return None

    def detect_end_of_execution(self, line):
        """Detect end of execution marker"""
        return "##end_of_execution##" in line

    def is_installed(self):
        """Check if R is installed"""
        try:
            subprocess.run(
                ["Rscript", "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
            return True
        except (subprocess.SubprocessError, FileNotFoundError):
            return False

    def installed_version(self):
        """Get the installed version of R"""
        try:
            result = subprocess.run(
                ["Rscript", "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,
            )
            # R version info is typically in stderr
            version_output = result.stderr or result.stdout
            if version_output:
                # Format: "R scripting front-end version X.Y.Z"
                return version_output.split()[5]
            return None
        except (subprocess.SubprocessError, FileNotFoundError):
            return None
