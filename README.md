# Sample Dashboard

A simple interactive web dashboard built with [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/python/). It visualizes the classic Iris dataset as a scatter plot of sepal width vs. sepal length, colored by species.

## Features

- Interactive scatter plot powered by Plotly
- Clean, centered layout with a page title
- Debug mode enabled for local development

## Prerequisites

- Python 3.8 or newer
- pip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/baruchfa/project2.git
   cd project2
   ```

2. Install the required packages:

   ```bash
   pip install dash plotly pandas
   ```

## Usage

Run the dashboard:

```bash
python test.py
```

Open your browser and go to [http://127.0.0.1:8050](http://127.0.0.1:8050) to view the app.

Press `Ctrl+C` in the terminal to stop the server.

## Project Structure

```
project2/
├── test.py      # Dash app entry point
└── README.md
```

## Dependencies

| Package  | Purpose                          |
| -------- | -------------------------------- |
| dash     | Web application framework        |
| plotly   | Interactive charts and figures   |
| pandas   | Data handling (via Plotly)       |

## License

This project is provided as-is for learning and demonstration purposes.
