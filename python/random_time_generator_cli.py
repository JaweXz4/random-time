#!/usr/bin/env python3
"""
Random Time Generator - CLI Version
A command-line tool that generates random times between specified min/max values.
"""

import random
from typing import Optional, Tuple


class TimeRange:
    """Represents a time in hours, minutes, and seconds."""
    
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def to_seconds(self) -> int:
        """Convert time to total seconds."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    @staticmethod
    def from_seconds(total_seconds: int) -> 'TimeRange':
        """Convert total seconds to TimeRange object."""
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return TimeRange(hours, minutes, seconds)
    
    def __str__(self) -> str:
        """Format as readable string."""
        return f"{self.hours}h {self.minutes}m {self.seconds}s"


class RandomTimeGenerator:
    """Generates random times between specified ranges."""
    
    @staticmethod
    def validate_time_input(hours: str, minutes: str, seconds: str) -> Tuple[bool, Optional[str], Optional[TimeRange]]:
        """Validate time input values."""
        try:
            h = int(hours) if hours else 0
            m = int(minutes) if minutes else 0
            s = int(seconds) if seconds else 0
            
            if h < 0 or m < 0 or s < 0:
                return False, "Time values cannot be negative.", None
            
            if m >= 60 or s >= 60:
                return False, "Minutes and seconds must be less than 60.", None
            
            return True, None, TimeRange(h, m, s)
        
        except ValueError:
            return False, "Please enter valid numbers for all time fields.", None
    
    @staticmethod
    def generate_random_time(min_time: TimeRange, max_time: TimeRange) -> Tuple[bool, Optional[str], Optional[str]]:
        """Generate random time between min and max."""
        min_seconds = min_time.to_seconds()
        max_seconds = max_time.to_seconds()
        
        if min_seconds > max_seconds:
            return False, "Minimum time cannot be greater than maximum time.", None
        
        random_seconds = random.randint(min_seconds, max_seconds)
        result_time = TimeRange.from_seconds(random_seconds)
        
        return True, None, str(result_time)
    
    def run_interactive(self):
        """Run the application in interactive mode."""
        print("\n" + "="*50)
        print("  Random Time Generator - CLI".center(50))
        print("="*50 + "\n")
        
        # Get minimum time
        print("Enter MINIMUM time:")
        min_hours = input("  Hours (default 1): ") or "1"
        min_minutes = input("  Minutes (default 0): ") or "0"
        min_seconds = input("  Seconds (default 0): ") or "0"
        
        valid, error, min_time = self.validate_time_input(min_hours, min_minutes, min_seconds)
        if not valid:
            print(f"\n❌ Error: {error}")
            return
        
        # Get maximum time
        print("\nEnter MAXIMUM time:")
        max_hours = input("  Hours (default 3): ") or "3"
        max_minutes = input("  Minutes (default 0): ") or "0"
        max_seconds = input("  Seconds (default 0): ") or "0"
        
        valid, error, max_time = self.validate_time_input(max_hours, max_minutes, max_seconds)
        if not valid:
            print(f"\n❌ Error: {error}")
            return
        
        # Generate random time
        success, error, result = self.generate_random_time(min_time, max_time)
        if success:
            print("\n" + "-"*50)
            print(f"Minimum Time:  {min_time}")
            print(f"Maximum Time:  {max_time}")
            print("-"*50)
            print(f"Random Time:   {result}")
            print("-"*50 + "\n")
        else:
            print(f"\n❌ Error: {error}\n")
    
    def run_example(self):
        """Run example with predefined values."""
        print("\n" + "="*50)
        print("  Random Time Generator - Example".center(50))
        print("="*50 + "\n")
        
        min_time = TimeRange(1, 0, 0)
        max_time = TimeRange(3, 0, 0)
        
        print(f"Generating random times between {min_time} and {max_time}\n")
        
        for i in range(5):
            success, error, result = self.generate_random_time(min_time, max_time)
            print(f"  Generated Time {i+1}: {result}")
        
        print()


def main():
    """Main entry point."""
    generator = RandomTimeGenerator()
    
    print("\nRandom Time Generator")
    print("1. Interactive Mode")
    print("2. Run Examples")
    print("3. Exit")
    
    choice = input("\nSelect an option (1-3): ").strip()
    
    if choice == '1':
        generator.run_interactive()
    elif choice == '2':
        generator.run_example()
    elif choice == '3':
        print("\nGoodbye!\n")
    else:
        print("\n❌ Invalid option. Please select 1, 2, or 3.\n")


if __name__ == '__main__':
    main()
