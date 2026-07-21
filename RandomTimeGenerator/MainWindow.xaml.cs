using System;
using System.Windows;
using System.Windows.Input;

namespace RandomTimeGenerator
{
    public partial class MainWindow : Window
    {
        private Random random = new Random();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void GenerateButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                // Parse input values
                if (!int.TryParse(MinHours.Text, out int minHours) ||
                    !int.TryParse(MinMinutes.Text, out int minMinutes) ||
                    !int.TryParse(MinSeconds.Text, out int minSeconds) ||
                    !int.TryParse(MaxHours.Text, out int maxHours) ||
                    !int.TryParse(MaxMinutes.Text, out int maxMinutes) ||
                    !int.TryParse(MaxSeconds.Text, out int maxSeconds))
                {
                    ShowError("Please enter valid numbers for all time fields.");
                    return;
                }

                // Validate time values
                if (minHours < 0 || minMinutes < 0 || minSeconds < 0 ||
                    maxHours < 0 || maxMinutes < 0 || maxSeconds < 0)
                {
                    ShowError("Time values cannot be negative.");
                    return;
                }

                if (minMinutes >= 60 || minSeconds >= 60 ||
                    maxMinutes >= 60 || maxSeconds >= 60)
                {
                    ShowError("Minutes and seconds must be less than 60.");
                    return;
                }

                // Convert to total seconds
                int minTotalSeconds = minHours * 3600 + minMinutes * 60 + minSeconds;
                int maxTotalSeconds = maxHours * 3600 + maxMinutes * 60 + maxSeconds;

                if (minTotalSeconds > maxTotalSeconds)
                {
                    ShowError("Minimum time cannot be greater than maximum time.");
                    return;
                }

                // Generate random time
                int randomTotalSeconds = random.Next(minTotalSeconds, maxTotalSeconds + 1);

                // Convert back to hours, minutes, seconds
                int resultHours = randomTotalSeconds / 3600;
                int resultMinutes = (randomTotalSeconds % 3600) / 60;
                int resultSeconds = randomTotalSeconds % 60;

                // Display result
                string resultText = $"{resultHours}h {resultMinutes}m {resultSeconds}s";
                ResultText.Text = resultText;
                StatusText.Text = "✓ Time generated successfully!";
                StatusText.Foreground = System.Windows.Media.Brushes.Green;
            }
            catch (Exception ex)
            {
                ShowError($"An error occurred: {ex.Message}");
            }
        }

        private void CopyButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                string resultText = ResultText.Text;
                if (resultText == "—")
                {
                    ShowError("Please generate a time first.");
                    return;
                }

                Clipboard.SetText(resultText);
                StatusText.Text = "✓ Copied to clipboard!";
                StatusText.Foreground = System.Windows.Media.Brushes.Green;
            }
            catch (Exception ex)
            {
                ShowError($"Failed to copy: {ex.Message}");
            }
        }

        private void NumberOnly_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            // Allow only numeric input
            e.Handled = !IsNumeric(e.Text);
        }

        private bool IsNumeric(string text)
        {
            return int.TryParse(text, out _);
        }

        private void ShowError(string message)
        {
            StatusText.Text = "✗ " + message;
            StatusText.Foreground = System.Windows.Media.Brushes.Red;
        }
    }
}
