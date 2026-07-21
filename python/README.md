# Random Time Generator - Python Version

Python implementations of the Random Time Generator application with both CLI and GUI versions.

## Features

- ⏱️ Generate random times between custom min/max ranges
- 🖥️ GUI and CLI interfaces available
- 🎨 Modern and intuitive user interface
- 📋 Copy generated time to clipboard (GUI)
- ✅ Input validation and error handling
- 🚀 Pure Python implementation

## Requirements

- Python 3.7 or higher
- PySimpleGUI 4.60.5+ (GUI only)

## Installation

### 1. Install Python

Download and install Python from [python.org](https://www.python.org/downloads/)

### 2. Install Dependencies

```bash
cd python
pip install -r requirements.txt
```

## Usage

### GUI Version (Recommended)

```bash
python random_time_generator_gui.py
```

**Features:**
- Clean, modern interface
- Input fields for hours, minutes, seconds
- Generate and copy buttons
- Real-time status messages
- Reset functionality

### CLI Version

```bash
python random_time_generator_cli.py
```

**Modes:**
1. **Interactive Mode** - Enter your own min/max times
2. **Example Mode** - See 5 random generations (1h to 3h)
3. **Exit** - Close the application

## Example

### GUI Example
1. Set Minimum Time: 1h 0m 0s
2. Set Maximum Time: 3h 0m 0s
3. Click "Generate Random Time"
4. Result: 2h 28m 49s
5. Click "Copy to Clipboard"

### CLI Example
```
Enter MINIMUM time:
  Hours (default 1): 1
  Minutes (default 0): 0
  Seconds (default 0): 0

Enter MAXIMUM time:
  Hours (default 3): 3
  Minutes (default 0): 0
  Seconds (default 0): 0

--------------------------------------------------
Minimum Time:  1h 0m 0s
Maximum Time:  3h 0m 0s
--------------------------------------------------
Random Time:   2h 28m 49s
--------------------------------------------------
```

## Project Structure

```
python/
├── random_time_generator_gui.py    # GUI application
├── random_time_generator_cli.py    # CLI application
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## Architecture

### TimeRange Class
- Represents a time with hours, minutes, seconds
- Methods:
  - `to_seconds()` - Convert to total seconds
  - `from_seconds()` - Convert from seconds
  - `__str__()` - Format as readable string

### RandomTimeGenerator Class
- `validate_time_input()` - Validate time values
- `generate_random_time()` - Generate random time between ranges

### GUI Features
- PySimpleGUI based interface
- Event-driven architecture
- Status messages with color coding
- Clipboard integration

## Error Handling

The application validates:
- Non-negative time values
- Minutes and seconds < 60
- Minimum time ≤ Maximum time
- Valid numeric input

## License

MIT License - see LICENSE file for details

## Author

JaweXz4
