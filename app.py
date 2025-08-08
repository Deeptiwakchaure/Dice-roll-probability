from flask import Flask, render_template, request, redirect, url_for, session
import random
import numpy as np
import decimal
import os  # Added for environment variables

app = Flask(__name__)
# Updated to use environment variable for secret key
app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_here')  

# Constants
FACES = 6
MOD = 1000000007

# Initialize DP table
dp = np.zeros((55, 55))

def no_of_ways(faces, dice_count, target_sum):
    """Calculate the number of ways to achieve a target sum with given dice."""
    dp = [[0] * (target_sum + 1) for _ in range(dice_count + 1)]
    dp[0][0] = 1
    for i in range(1, dice_count + 1):
        for j in range(1, target_sum + 1):
            for k in range(1, faces + 1):
                if k <= j:
                    dp[i][j] += dp[i - 1][j - k]
    return dp[dice_count][target_sum]

def probability_of_sum(dice_count, target_sum):
    """Calculate the probability of achieving a target sum with given dice."""
    ways_to_get_k = no_of_ways(FACES, dice_count, target_sum)
    total_ways = FACES ** dice_count
    prob = ways_to_get_k / total_ways
    
    # Format in scientific notation
    ways_str = format(decimal.Decimal(ways_to_get_k), '.1e')
    total_str = format(decimal.Decimal(total_ways), '.1e')
    
    # Reset DP table
    for i in range(55):
        for j in range(55):
            dp[i][j] = -1
    
    return prob, ways_str, total_str

def roll_dice(dice_count):
    """Simulate rolling dice and return results."""
    dice_sum = 0
    results = []
    for i in range(dice_count):
        dice_result = random.randint(1, FACES)
        dice_sum += dice_result
        results.append(dice_result)
    return dice_sum, results

@app.route('/')
def index():
    """Main page to start the game."""
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    """Handle the initial choice to roll dice."""
    choice = request.form.get('choice')
    if choice == 'Yes':
        return redirect(url_for('ask_dice_count'))
    else:
        return render_template('goodbye.html')

@app.route('/ask_dice_count')
def ask_dice_count():
    """Ask user for the number of dice to roll."""
    return render_template('ask_dice_count.html')

@app.route('/set_dice_count', methods=['POST'])
def set_dice_count():
    """Process the dice count input."""
    try:
        dice_count = int(request.form.get('dice_count'))
        if dice_count <= 0:
            return render_template('ask_dice_count.html', error="Please enter a positive number of dice.")
        session['dice_count'] = dice_count
        return redirect(url_for('ask_target_sum'))
    except ValueError:
        return render_template('ask_dice_count.html', error="Please enter a valid integer.")

@app.route('/ask_target_sum')
def ask_target_sum():
    """Ask if user has a target sum in mind."""
    return render_template('ask_target_sum.html')

@app.route('/handle_target_sum', methods=['POST'])
def handle_target_sum():
    """Process the target sum choice."""
    choice = request.form.get('choice')
    if choice == 'Yes':
        return redirect(url_for('ask_target_sum_value'))
    else:
        return redirect(url_for('roll_dice_route'))  # Fixed: changed from roll_dice to roll_dice_route

@app.route('/ask_target_sum_value')
def ask_target_sum_value():
    """Ask user for the target sum value."""
    dice_count = session.get('dice_count', 1)
    min_sum = dice_count
    max_sum = dice_count * FACES
    return render_template('ask_target_sum_value.html', 
                          min_sum=min_sum, 
                          max_sum=max_sum,
                          dice_count=dice_count)  # Added dice_count for template

@app.route('/show_probability', methods=['POST'])
def show_probability():
    """Calculate and display probability for target sum."""
    try:
        target_sum = int(request.form.get('target_sum'))
        dice_count = session.get('dice_count', 1)
        
        # Validate target sum
        if target_sum < dice_count or target_sum > dice_count * FACES:
            min_sum = dice_count
            max_sum = dice_count * FACES
            return render_template('ask_target_sum_value.html', 
                                  error=f"The sum must be between {min_sum} and {max_sum}",
                                  min_sum=min_sum, 
                                  max_sum=max_sum,
                                  dice_count=dice_count)  # Added dice_count for template
        
        prob, ways_str, total_str = probability_of_sum(dice_count, target_sum)
        
        return render_template('show_probability.html', 
                              dice_count=dice_count, 
                              target_sum=target_sum,
                              prob=prob,
                              ways_str=ways_str,
                              total_str=total_str)
    except ValueError:
        dice_count = session.get('dice_count', 1)
        min_sum = dice_count
        max_sum = dice_count * FACES
        return render_template('ask_target_sum_value.html', 
                              error="Please enter a valid integer.",
                              min_sum=min_sum, 
                              max_sum=max_sum,
                              dice_count=dice_count)  # Added dice_count for template

@app.route('/roll_dice')
def roll_dice_route():
    """Roll the dice and display results."""
    dice_count = session.get('dice_count', 1)
    dice_sum, results = roll_dice(dice_count)
    prob, ways_str, total_str = probability_of_sum(dice_count, dice_sum)
    
    return render_template('roll_result.html',
                          dice_count=dice_count,
                          dice_sum=dice_sum,
                          results=results,
                          prob=prob,
                          ways_str=ways_str,
                          total_str=total_str)

@app.route('/roll_again', methods=['POST'])
def roll_again():
    """Handle choice to roll again or not."""
    choice = request.form.get('choice')
    if choice == 'Yes':
        return redirect(url_for('ask_dice_count'))
    else:
        return render_template('goodbye.html')

# Updated for production deployment
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get port from environment
    debug = os.environ.get('DEBUG', 'False') == 'True'  # Get debug mode from environment
    app.run(host='0.0.0.0', port=port, debug=debug)  # Run with production settings