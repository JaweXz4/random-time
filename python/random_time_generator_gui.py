#!/usr/bin/env python3
"""
Random Time Generator - GUI Version
A Windows desktop application that generates random times between specified min/max values.
"""

import PySimpleGUI as sg
import random
import sys
from typing import Tuple, Optional


class TimeRange:
    """Represents a time range with hours, minutes, and seconds."""
    
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
    
    def __init__(self):
        self.last_generated_time: Optional[str] = None
        self.setup_theme()
    
    @staticmethod
    def setup_theme():
        """Configure PySimpleGUI theme."""
        sg.theme('LightBlue2')
        sg.set_options(font=('Arial', 11))
    
    def validate_time_input(self, hours: str, minutes: str, seconds: str) -> Tuple[bool, Optional[str], Optional[TimeRange]]:
        """Validate time input values."""
        try:
            h = int(hours) if hours else 0
            m = int(minutes) if minutes else 0
            s = int(seconds) if seconds else 0
            
            if h < 0 or m < 0 or s < 0:
                return False, "❌ Time values cannot be negative.", None
            
            if m >= 60 or s >= 60:
                return False, "❌ Minutes and seconds must be less than 60.", None
            
            return True, None, TimeRange(h, m, s)
        
        except ValueError:
            return False, "❌ Please enter valid numbers for all time fields.", None
    
    def generate_random_time(self, min_time: TimeRange, max_time: TimeRange) -> Tuple[bool, Optional[str], Optional[str]]:
        """Generate random time between min and max."""
        min_seconds = min_time.to_seconds()
        max_seconds = max_time.to_seconds()
        
        if min_seconds > max_seconds:
            return False, "❌ Minimum time cannot be greater than maximum time.", None
        
        random_seconds = random.randint(min_seconds, max_seconds)
        result_time = TimeRange.from_seconds(random_seconds)
        self.last_generated_time = str(result_time)
        
        return True, None, str(result_time)
    
    def create_window(self):
        """Create and return the main window layout."""
        
        # Define the layout
        layout = [
            # Title
            [sg.Text('Random Time Generator', font=('Arial', 28, 'bold'), justification='center', expand_x=True)],
            [sg.Text('')],  # Spacer
            
            # Minimum Time Section
            [sg.Frame('Minimum Time', [
                [sg.Column([
                    [sg.Text('Hours', font=('Arial', 11, 'bold'))],
                    [sg.InputText('1', key='min_hours', size=(10, 1), font=('Arial', 12))]
                ], vertical_alignment='top'),
                sg.Column([
                    [sg.Text('Minutes', font=('Arial', 11, 'bold'))],
                    [sg.InputText('0', key='min_minutes', size=(10, 1), font=('Arial', 12))]
                ], vertical_alignment='top'),
                sg.Column([
                    [sg.Text('Seconds', font=('Arial', 11, 'bold'))],
                    [sg.InputText('0', key='min_seconds', size=(10, 1), font=('Arial', 12))]
                ], vertical_alignment='top')]
            ], expand_x=True)],
            
            [sg.Text('')],  # Spacer
            
            # Maximum Time Section
            [sg.Frame('Maximum Time', [
                [sg.Column([
                    [sg.Text('Hours', font=('Arial', 11, 'bold'))],
                    [sg.InputText('3', key='max_hours', size=(10, 1), font=('Arial', 12))]
                ], vertical_alignment='top'),
                sg.Column([
                    [sg.Text('Minutes', font=('Arial', 11, 'bold'))],
                    [sg.InputText('0', key='max_minutes', size=(10, 1), font=('Arial', 12))]
                ], vertical_alignment='top'),
                sg.Column([
                    [sg.Text('Seconds', font=('Arial', 11, 'bold'))],
                    [sg.InputText('0', key='max_seconds', size=(10, 1), font=('Arial', 12))]
                ], vertical_alignment='top')]
            ], expand_x=True)],
            
            [sg.Text('')],  # Spacer
            
            # Generate Button
            [sg.Button('Generate Random Time', key='generate', size=(30, 2), font=('Arial', 12, 'bold'), button_color=('white', '#3498DB'))],
            
            [sg.Text('')],  # Spacer
            
            # Result Section
            [sg.Frame('Result', [
                [sg.Text('Generated Time:', font=('Arial', 11, 'bold'))],
                [sg.Text('—', key='result', font=('Arial', 24, 'bold'), text_color='#27AE60', justification='center', expand_x=True)],
                [sg.Button('Copy to Clipboard', key='copy', size=(25, 1), font=('Arial', 11), button_color=('white', '#27AE60'))]
            ], expand_x=True)],
            
            [sg.Text('')],  # Spacer
            
            # Status Bar
            [sg.Multiline(size=(50, 3), key='status', disabled=True, background_color='#F0F0F0', font=('Arial', 10))],
            
            # Buttons
            [sg.Button('Exit', key='exit', size=(10, 1)), sg.Button('Reset', key='reset', size=(10, 1))]
        ]
        
        window = sg.Window(
            'Random Time Generator',
            layout,
            size=(600, 700),
            finalize=True,
            icon=None
        )
        
        # Make result text more prominent
        window['result'].update(text_color='#27AE60')
        
        return window
    
    def update_status(self, window, message: str, error: bool = False):
        """Update status message."""
        prefix = "❌" if error else "✓"
        status_text = f"{prefix} {message}"
        window['status'].update(status_text)
        
        if error:
            window['status'].update(text_color='red')
        else:
            window['status'].update(text_color='green')
    
    def run(self):
        """Run the application."""
        window = self.create_window()
        
        try:
            while True:
                event, values = window.read()
                
                if event == sg.WINDOW_CLOSED or event == 'exit':
                    break
                
                elif event == 'generate':
                    # Validate minimum time
                    valid, error, min_time = self.validate_time_input(
                        values['min_hours'],
                        values['min_minutes'],
                        values['min_seconds']
                    )
                    
                    if not valid:
                        self.update_status(window, error.replace('❌ ', ''), error=True)
                        continue
                    
                    # Validate maximum time
                    valid, error, max_time = self.validate_time_input(
                        values['max_hours'],
                        values['max_minutes'],
                        values['max_seconds']
                    )
                    
                    if not valid:
                        self.update_status(window, error.replace('❌ ', ''), error=True)
                        continue
                    
                    # Generate random time
                    success, error, result = self.generate_random_time(min_time, max_time)
                    
                    if success:
                        window['result'].update(value=result, text_color='#27AE60')
                        self.update_status(window, "Time generated successfully!")
                    else:
                        self.update_status(window, error.replace('❌ ', ''), error=True)
                
                elif event == 'copy':
                    if self.last_generated_time:
                        try:
                            window.write_event_value('-COPY-', self.last_generated_time)
                            # Use tkinter's clipboard
                            import tkinter as tk
                            root = tk.Tk()
                            root.withdraw()
                            root.clipboard_clear()
                            root.clipboard_append(self.last_generated_time)
                            root.update()
                            root.destroy()
                            self.update_status(window, "Copied to clipboard!")
                        except Exception as e:
                            self.update_status(window, f"Failed to copy: {str(e)}", error=True)
                    else:
                        self.update_status(window, "Please generate a time first", error=True)
                
                elif event == 'reset':
                    window['min_hours'].update('1')
                    window['min_minutes'].update('0')
                    window['min_seconds'].update('0')
                    window['max_hours'].update('3')
                    window['max_minutes'].update('0')
                    window['max_seconds'].update('0')
                    window['result'].update('—')
                    window['status'].update('')
                    self.last_generated_time = None
        
        finally:
            window.close()


def main():
    """Main entry point."""
    app = RandomTimeGenerator()
    app.run()


if __name__ == '__main__':
    main()
