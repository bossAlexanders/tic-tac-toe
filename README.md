PEP8 Compliance:

Fixed wildcard import (from tkinter import * → import tkinter as tk)

Consistent spacing around operators and after commas

Proper line wrapping for long lines

Descriptive variable names (e.g., draw → draw_count)

Type Hints Added:

Added type annotations for all function parameters and return values

Used proper typing imports (List, Tuple, Optional)

Annotated global variables in main section

English Documentation:

All docstrings translated to English with clear descriptions

Module-level docstring explaining the application

Detailed function documentation with parameter and return descriptions

Code Structure:

Split complex functions into smaller, focused functions

Created handle_win(), handle_draw(), switch_player(), update_statistics(), check_special_wins()

Improved function names for clarity

Moved GUI creation to create_gui() function

Improved Logic:

Fixed the win condition check to include non-empty check

Better separation of concerns

More maintainable and testable code structure

Visual Consistency:

Renamed variables for consistency (procent → percent)

Improved English labels in GUI

Maintained original color scheme and layout
