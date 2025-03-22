import os
import shutil
import re
import json
from concurrent.futures import ThreadPoolExecutor

def copy_logs(source_dir, destination_dir):
    """Copies log files from the source directory to the destination directory."""
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    for file_name in os.listdir(source_dir):
        if file_name.endswith(".log") or file_name.endswith(".json"):
            shutil.copy(os.path.join(source_dir, file_name), os.path.join(destination_dir, file_name))
    print("Log files copied successfully.")

def extract_errors(log_file, error_output_file):
    """Extracts error messages from log files and stores them in a separate file."""
    error_patterns = [
        re.compile(r"ERROR.*"),  # Matches general errors
        re.compile(r"Exception:.*"),  # Matches exceptions
        re.compile(r"[Ee]rror[: ].*"),  # Matches errors in different formats
    ]
    
    errors = []
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            if any(pattern.search(line) for pattern in error_patterns):
                errors.append(line.strip())
                print(line.strip())
    
    if errors:
        with open(error_output_file, 'a', encoding='utf-8') as error_log:
            error_log.write("\n".join(errors) + "\n")
    print(f"Errors extracted from {log_file} and stored in {error_output_file}.")

def format_log_entry(log_entry):
    """Formats log entries based on predefined patterns."""
    if log_entry.strip().startswith("{") and log_entry.strip().endswith("}"):
        try:
            log_json = json.loads(log_entry)
            return json.dumps(log_json, indent=4)  # Pretty-print JSON logs
        except json.JSONDecodeError:
            return log_entry.strip()
    else:
        return re.sub(r'\s+', ' ', log_entry.strip())  # Normalize spacing

def process_logs(source_dir, destination_dir):
    """Processes all logs by copying, extracting errors, and formatting entries."""
    copy_logs(source_dir, destination_dir)
    
    error_output_file = os.path.join(destination_dir, "error_logs.txt")
    
    with ThreadPoolExecutor() as executor:
        log_files = [os.path.join(destination_dir, f) for f in os.listdir(destination_dir) if f.endswith(".log") or f.endswith(".json")]
        executor.map(lambda log_file: extract_errors(log_file, error_output_file), log_files)
    
    formatted_logs_output = os.path.join(destination_dir, "formatted_logs.txt")
    with open(formatted_logs_output, 'w', encoding='utf-8') as formatted_log_file:
        for log_file in log_files:
            with open(log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    formatted_log_file.write(format_log_entry(line) + "\n")
    print(f"Formatted logs stored in {formatted_logs_output}.")

if __name__ == "__main__":
    source_directory = "logs/source"
    destination_directory = "logs/processed"
    process_logs(source_directory, destination_directory)
