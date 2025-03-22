## Log Analysis Script

This script automates log analysis tasks, including copying Apache, Spark, and Hadoop log files, extracting error messages, and formatting log entries.

### Features:
- Copies log files from a source directory to a destination directory.
- Extracts error messages from log files and saves them in `error_logs.txt`.
- Formats log entries and stores them in `formatted_logs.txt`.
- Supports multiple log file formats (text-based logs, JSON logs).
- Processes multiple files concurrently.

### Pre-requirements:
- Python 3.x
- Bash (for automation script)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/bevcikandrij125/log-analysis.git
   cd log-analysis
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Place log files in the `logs/source/` directory.
2. Run the script using Python:
   ```bash
   python log_analysis_script.py
   ```
   Or run using the Bash script:
   ```bash
   bash run_log_analysis.sh
   ```
3. Processed logs will be available in `logs/processed/`:
   - Extracted errors: `error_logs.txt`
   - Formatted logs: `formatted_logs.txt`

### File Structure
```
log-analysis/
│-- logs/
│   │-- source/      # Place raw log files here
│   │-- processed/   # Processed log files will be stored here
│-- log_analysis_script.py
│-- run_log_analysis.sh
│-- requirements.txt
│-- README.md
```