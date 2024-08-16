import sys  # For interacting with system-specific parameters
import datetime  # For handling dates and times
import re  # For performing regular expression operations
from collections import namedtuple, deque, Counter  # For specialized container datatypes
import itertools  # For creating efficient iterators
import functools  # For higher-order functions
import json  # For parsing and generating JSON
import argparse  # For command-line argument parsing
import logging  # For logging information
import unittest  # For built-in testing framework
import multiprocessing  # For parallel execution
import subprocess  # For executing and interacting with subprocesses
from pathlib import Path  # For object-oriented filesystem paths
import http.client  # For HTTP protocol client (optional, if needed for fetching logs)
import socket  # For low-level networking interface (optional, if needed for fetching logs)
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For scientific computing with arrays
import matplotlib.pyplot as plt  # For plotting and visualization

# Define a namedtuple for storing log entry information
LogEntry = namedtuple('LogEntry', ['timestamp', 'request_type', 'response_time', 'status_code'])

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_log_file(file_path):
    """Parse a JSON log file and return a list of LogEntry namedtuples."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    log_entries = []
    for entry in data['logs']:
        timestamp = datetime.datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S')
        request_type = entry['request_type']
        response_time = entry['response_time']
        status_code = entry['status_code']
        log_entries.append(LogEntry(timestamp, request_type, response_time, status_code))
    
    return log_entries

def analyze_logs(log_entries):
    """Analyze log entries and return statistics."""
    request_types = Counter(entry.request_type for entry in log_entries)
    response_times = [entry.response_time for entry in log_entries]
    status_codes = Counter(entry.status_code for entry in log_entries)

    avg_response_time = np.mean(response_times)
    error_rate = sum(code.startswith('5') for code in status_codes) / len(log_entries) * 100

    return request_types, avg_response_time, error_rate

def visualize_data(request_types, avg_response_time, error_rate):
    """Visualize the data with matplotlib."""
    # Plot request types
    plt.figure(figsize=(10, 5))
    plt.bar(request_types.keys(), request_types.values())
    plt.xlabel('Request Type')
    plt.ylabel('Frequency')
    plt.title('Request Types Frequency')
    plt.savefig('request_types.png')
    plt.close()

    # Plot average response time
    plt.figure(figsize=(5, 5))
    plt.bar(['Average Response Time'], [avg_response_time])
    plt.ylabel('Time (ms)')
    plt.title('Average Response Time')
    plt.savefig('avg_response_time.png')
    plt.close()

    # Print error rate
    print(f"Error Rate: {error_rate:.2f}%")

def main():
    """Main function to handle the process."""
    parser = argparse.ArgumentParser(description='Analyze web service logs.')
    parser.add_argument('log_file', type=Path, help='Path to the JSON log file')
    args = parser.parse_args()

    logging.info(f"Parsing log file: {args.log_file}")
    log_entries = parse_log_file(args.log_file)

    logging.info("Analyzing log entries")
    request_types, avg_response_time, error_rate = analyze_logs(log_entries)

    logging.info("Visualizing data")
    visualize_data(request_types, avg_response_time, error_rate)

    logging.info("Log analysis completed.")

if __name__ == '__main__':
    main()

# Unit tests
class TestLogAnalysis(unittest.TestCase):
    def setUp(self):
        self.log_entries = [
            LogEntry(datetime.datetime(2024, 8, 8, 10, 0, 0), 'GET', 123, '200'),
            LogEntry(datetime.datetime(2024, 8, 8, 10, 5, 0), 'POST', 456, '500'),
            LogEntry(datetime.datetime(2024, 8, 8, 10, 10, 0), 'GET', 789, '200'),
        ]

    def test_analyze_logs(self):
        request_types, avg_response_time, error_rate = analyze_logs(self.log_entries)
        self.assertEqual(request_types['GET'], 2)
        self.assertAlmostEqual(avg_response_time, 456.0)
        self.assertAlmostEqual(error_rate, 33.33)

if __name__ == '__main__':
    unittest.main()
