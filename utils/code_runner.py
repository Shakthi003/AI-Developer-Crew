import subprocess
import sys
from pathlib import Path


def run_python_file(file_path: str):
    """
    Runs a Python file as a subprocess and streams its output live.
    Works inside virtual environments too.
    """
    file = Path(file_path)
    if not file.exists():
        print(f"❌ File not found: {file}")
        return

    print(f"🚀 Running: {file}\n{'-'*60}")

    try:
        # Run the Python file using the current interpreter
        result = subprocess.run(
            [sys.executable, str(file)],
            capture_output=True,
            text=True
        )

        # Display stdout and stderr
        if result.stdout:
            print("✅ Output:\n", result.stdout)
        if result.stderr:
            print("⚠️ Errors:\n", result.stderr)

    except Exception as e:
        print(f"❌ Exception while running {file.name}: {e}")

    print('-'*60)
    print("🏁 Execution completed.")


if __name__ == "__main__":
    # Example usage (you can change the path as needed)
    run_python_file("app.py")
