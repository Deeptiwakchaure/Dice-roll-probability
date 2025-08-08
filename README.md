# Dice Probability Game

A web-based interactive dice probability calculator with realistic rolling animations and probability analysis.

## Features

- **Interactive Dice Rolling**: Roll multiple dice with realistic animations.
- **Probability Calculations**: Calculate the probability of achieving a specific target sum.
- **Visual Feedback**: Animated dice, progress bars, and confetti for high-probability rolls.
- **Responsive Design**: Works on both desktop and mobile devices.
- **User-Friendly Interface**: Clean and intuitive UI.

## Technologies Used

**Backend**
- Python (Flask)

**Frontend**
- HTML5, CSS3, JavaScript
- Bootstrap 4.5.2 for responsive design
- Font Awesome for icons

**Libraries**
- NumPy for probability calculations
- Decimal for precise number formatting

## Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/y/Deeptiwakchaure/Dice-roll-probability.git
   cd dice-probability-game
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing:

bash
Copy
Edit
pip install flask numpy
Running the Application
Activate the virtual environment (if created).

Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
Application Flow
Start Page – Choose to start the game or exit.

Dice Count – Enter the number of dice (1–50).

Target Sum – If yes, enter the sum and view the probability. If no, proceed to roll.

Dice Roll – Animated results with total, average, and probability.

Play Again – Option to roll again or exit.

Project Structure
csharp
Copy
Edit
dice-probability-game/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/                # CSS, JS, and image files
│   └── images/
│       └── sleepy.png
└── templates/             # HTML templates
    ├── index.html
    ├── ask_dice_count.html
    ├── ask_target_sum.html
    ├── ask_target_sum_value.html
    ├── show_probability.html
    ├── roll_result.html
    └── goodbye.html
Screenshots
Start Page


Dice Count Selection


Target Sum Selection


Probability Calculation


Dice Roll Result


Future Enhancements
Support for multiple dice types (d4, d8, d10, d12, d20)

User accounts to save history

Sound effects

Multiplayer mode

Advanced charts and statistics

Mobile app version

Contributing
Fork the repository.

Create a feature branch:

bash
Copy
Edit
git checkout -b feature/your-feature
Commit your changes:

bash
Copy
Edit
git commit -m "Add your feature"
Push to the branch:

bash
Copy
Edit
git push origin feature/your-feature
Open a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Bootstrap for responsive UI

Font Awesome for icons

Flask community for documentation

