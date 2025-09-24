# Copilot Instructions for BookBot

## Project Overview
BookBot is a simple Python project that analyzes the text of books. The current implementation processes `frankenstein.txt` to count the total number of words. The project is structured for learning and experimentation, with a focus on clarity and simplicity.

## Architecture & Data Flow
- **Entry Point:** `main.py` is the main script. It imports and calls functions from other modules.
- **Text Processing:**
  - `main.py` defines `get_book_text(path_to_file)` to read the contents of a book file.
  - It imports `count` from `stats.py` and calls it.
  - `stats.py` expects `get_book_text` to be available in its scope (currently, this is a missing dependency; see below).
  - The book file is located at `books/frankenstein.txt`.
- **Output:** The result is printed to the console: `Found <N> total words`.

## Key Files & Directories
- `main.py`: Entry point, reads book text, triggers analysis.
- `stats.py`: Contains analysis logic (word counting).
- `books/`: Directory for book text files.
- `README.md`: Project overview (minimal).

## Developer Workflows
- **Run the project:**
  ```bash
  python3 main.py
  ```
- **Add new books:** Place `.txt` files in the `books/` directory and update code to reference them.
- **Extend analysis:** Add new functions to `stats.py` and call them from `main.py`.

## Project-Specific Patterns & Conventions
- All book file paths are absolute and hardcoded; refactor to use relative paths for portability.
- Functions are defined at module level; no classes or advanced patterns are used.
- No external dependencies; pure Python standard library.
- Minimal error handling; add checks for missing files or invalid paths if extending.

## Integration Points & Known Issues
- `stats.py` uses `get_book_text` but does not import it; ensure shared functions are imported or refactored for clarity.
- No test suite or build system is present; add tests in future for reliability.

## Example Pattern
```python
# main.py
from stats import count
count()
```

## Recommendations for AI Agents
- When adding new analysis, keep logic in `stats.py` and call from `main.py`.
- Use relative paths for book files to improve portability.
- Document new workflows in this file and in `README.md`.
- Maintain simplicity and readability; this is a learning project.
