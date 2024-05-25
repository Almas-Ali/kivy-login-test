# Kivy Login Test

A basic account management in kivy multi screen with database support. I have used sqlite3 database which comes with by default with Python. To manage database efficiently I have used `peewee` ORM.

Folder structure of this project.

```bash
.
├── design.kv
├── kivy_app.db
├── main.py
├── models.py
├── README.md
└── requirements.txt
```

## Installation

To install the required packages run the following command.

```bash
# Clone the repository
git clone https://github.com/Almas-Ali/kivy-login-test login_app

# Change the directory
cd login_app

# Create a virtual environment (optional)
python -m venv .venv

# Activate the virtual environment (Windows)
.venv\Scripts\activate

# Activate the virtual environment (Linux)
source .venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Run the application
python main.py
```

Created by [Md. Almas Ali][almas]

[almas]: https://github.com/Almas-Ali "Md. Almas Ali"
