# WhatsApp Chat Analyzer

A Streamlit web application that analyzes WhatsApp chat data and provides insights through visualizations.

## Features

- Upload WhatsApp chat export files (supports both Android and iPhone formats)
- View message statistics (total messages, words, media, links)
- Analyze monthly timeline of chat activity
- View activity patterns by day and month
- Generate weekly activity heatmap
- Identify most active users in group chats
- Analyze word clouds and common words
- Emoji analysis

## Local Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository or download the source code
2. Open a terminal/command prompt in the project directory
3. Install the required dependencies:

```
pip install -r requirements.txt
```

### Running the Application

1. Make sure port 8501 is not in use
2. Run the following command in the terminal:

```
streamlit run app.py
```

3. Open your web browser and navigate to http://localhost:8501

## How to Use

1. Select your phone type (Android or iPhone) from the sidebar
2. Upload your WhatsApp chat export file (.txt format)
3. Select a user from the dropdown or choose 'overall' for group analysis
4. Click "Show Analysis" to view the results

## Deployment

For deployment instructions, please refer to the [Deployment Guide](DEPLOYMENT_GUIDE.md).

## License

This project is open source and available under the MIT License.

## Acknowledgements

- Streamlit for the web application framework
- Matplotlib and Seaborn for data visualization
