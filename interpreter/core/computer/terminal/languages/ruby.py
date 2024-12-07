"""Ruby language support"""

import subprocess

from .subprocess_language import SubprocessLanguage


class Ruby(SubprocessLanguage):
    """Ruby programming language support"""

    file_extension = "rb"
    name = "Ruby"

    def __init__(self):
        super().__init__()
        self.start_cmd = ["ruby"]

    def preprocess_code(self, code):
        """Add end of execution marker"""
        # Add commands that tell us what line is being executed
        processed_code = code
        # Add end command (we'll be listening for this so we know when it ends)
        processed_code += '\nputs "##end_of_execution##"'
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
        """Check if Ruby is installed"""
        try:
            subprocess.run(
                ["ruby", "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
            return True
        except (subprocess.SubprocessError, FileNotFoundError):
            return False

    def installed_version(self):
        """Get the installed version of Ruby"""
        try:
            result = subprocess.run(
                ["ruby", "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,
            )
            # Ruby version info is in stdout
            version_output = result.stdout
            if version_output:
                # Format: "ruby X.Y.Z..."
                return version_output.split()[1]
            return None
        except (subprocess.SubprocessError, FileNotFoundError):
            return None
