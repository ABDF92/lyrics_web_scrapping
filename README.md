
# 🎵 Lyrics Scraper

This project allows you to search for a song on Megalobiz and retrieve its lyrics using web scraping. The lyrics are saved locally in a `.lrc` file.

## 📋 Features

- **Search for Songs**: Enter the name of the song to search for on Megalobiz.
- **Retrieve Lyrics**: Extract lyrics from the selected song page.
- **Save Lyrics**: Save the retrieved lyrics in a `.lrc` file for offline access.

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Ensure you have Python installed on your system.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abdf92/lyrics_web_scrapping.git
   cd lyrics_web_scrapping

2. **Install required libraries**:
    ```bash
    pip install requests beautifulsoup4

### Running the Script
    
1. **Navigate to the Project Directory:**
    ```bash
    cd lyrics-scraper

2. **Run the Script:**

    ```bash
    python lyrics_scraper.py

3. **Enter the Song Name:**
When prompted, enter the name of the song you want to search for.

4. **Select the Song from the List:**
Choose the correct song from the displayed list to fetch its lyrics.

5. **Lyrics Saved:**
The lyrics will be saved in a file named after the song in the project directory.

### 🛠️ Code Explanation
The script performs the following steps:

1. Get the Song Name: Prompts the user to enter the name of the song.

2. Construct Search URL: Creates a search URL for Megalobiz based on the song name.

3. Parse Search Results: Uses BeautifulSoup to parse the search results and extract song links.

4. Display Song Choices: Shows a list of matching songs for the user to choose from.

5. Retrieve Lyrics: Fetches the lyrics of the selected song from its page.

6. Save Lyrics: Saves the lyrics in a .lrc file.

### 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or bug fixes.
