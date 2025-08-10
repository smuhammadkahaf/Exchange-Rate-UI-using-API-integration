# Exchange Rate With UI

This project is a Python application that provides a graphical user interface (UI) for fetching and displaying currency exchange rates using an external API.

## Features
- Fetches real-time exchange rates using an API key
- User-friendly UI for selecting currencies and viewing rates
- Modular code structure with separate files for API logic, UI, and main execution

## API Key
You can obtain a free API key from [ExchangeRate-API](https://www.exchangerate-api.com/). Add your key to `API_Key.py`.

## File Structure
- `main.py`: Entry point for the application
- `API_Key.py`: Stores the API key used for accessing the exchange rate API
- `API_Logic.py`: Contains functions for making API requests and processing exchange rate data
- `UI.py`: Implements the graphical user interface
- `__pycache__/`: Python cache files (auto-generated)

## Requirements
- Python 3.7+
- `requests` library (for API calls)
- `tkinter` (for UI, included in standard Python distribution)

## Setup
1. Clone the repository or download the project files.
2. Install required packages:
   ```powershell
   pip install requests
   ```
3. Add your API key to `API_Key.py`.
4. Run the application:
   ```powershell
   python main.py
   ```

## Usage
- Launch the app and select the currencies you want to convert.
- View the latest exchange rates fetched from the API.

## License
This project is for learning purposes and you are free to use it.

## Author
smuhammadkahaf
