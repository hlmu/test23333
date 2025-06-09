#!/usr/bin/env python3
"""
Hello World Python Project
A simple demonstration of a basic Python application.
"""

def hello_world():
    """Print a hello world message."""
    return "Hello, World!"

def greet(name):
    """Greet a specific person."""
    return f"Hello, {name}!"

def main():
    """Main function to run the application."""
    print(hello_world())
    print(greet("Python Developer"))
    print("Welcome to this sample Python project!")

if __name__ == "__main__":
    main()