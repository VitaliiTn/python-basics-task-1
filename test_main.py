import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run_prog(given: str) -> str:
    """Запускає main.py, подає рядок на stdin і повертає stdout."""
    cp = subprocess.run(
        [sys.executable, str(ROOT / "main.py")],
        input=given,
        text=True,
        capture_output=True,
        timeout=2
    )
    assert cp.returncode == 0, f"Program exited with code {cp.returncode}. stderr:\n{cp.stderr}"
    return cp.stdout

def check(name: str):
    out = run_prog(name + "\n")
    # Перевіряємо точний формат без зайвих пробілів/рядків
    assert out.strip() == f"Привіт, {name}!", (
        f"Очікував: 'Привіт, {name}!'\nОтримав: '{out.strip()}'"
    )

def test_greeting_cyrillic():
    check("Іван")

def test_greeting_latin():
    check("Anna")
