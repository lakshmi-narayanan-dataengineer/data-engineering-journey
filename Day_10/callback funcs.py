"""
Callback Functions in Python
----------------------------
A Callback Function is a function passed as an argument to another function,
intended to be executed ("called back") at a specific point within that function.

Callbacks can be:
1. Synchronous: Executed immediately inside the host function.
2. Asynchronous / Event-driven: Executed after a delay or an event (e.g., button click).
"""

import time
import threading



# 1. Synchronous Callback (Immediate Execution)


def show_greeting():
    """Callback function to display a greeting."""
    print("Hi!, Hello!!")


def on_submit(callback):
    """
    Host function accepting a callback function.
    Executes the callback immediately after handling the event action.
    """
    print("Button clicked!")
    callback()  # Executing the callback function


print("--- 1. Synchronous Callback Example ---")
# Call the function directly (no print wrapper needed)
on_submit(show_greeting)


# 2. Asynchronous/Delayed Callback (Simulating Event Delay)


def notify_completion():
    """Callback function triggered when a task completes."""
    print("Task completed after delay!")


def run_delayed_task(callback, delay_seconds=2):
    """Simulates an asynchronous task that executes a callback after a delay."""
    print(f"Starting task... (will complete in {delay_seconds} seconds)")
    
    # Python thread timer simulates waiting for an event/delay
    timer = threading.Timer(delay_seconds, callback)
    timer.start()


print("\n--- 2. Delayed/Asynchronous Callback Example ---")
run_delayed_task(notify_completion, delay_seconds=2)