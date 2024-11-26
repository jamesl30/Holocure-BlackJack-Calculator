from flask import Flask, render_template, request

app = Flask(__name__)
# Define the Blackjack action calculator
def calculate(player_sum, player_aces, dealer_sum, dealer_aces):
    dp = [[[]*22]*22]*22 #dp[k][i][j] = probability dealer will have sum of i cards and j aces if you have a sum of k
    bribe_count = 0
    expected_value = 0
    odds_winning = 1
    rec_action = "HOLD"
    return expected_value, odds_winning, bribe_count, rec_action

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize default values
    player_sum = 12
    player_aces = 0
    dealer_sum = 12
    dealer_aces = 0
    
    if request.method == 'POST':
        
        # Get player hand and dealer's card from the form
        try:
            player_sum = int(request.form['player_sum'])
            player_aces = int(request.form['player_aces'])
            dealer_sum = int(request.form['dealer_sum'])
            dealer_aces = int(request.form['dealer_aces'])
                        
            # Calculate recommended action
            max_expected_value, max_odds_winning, max_bribe_count, rec_action = calculate(player_sum, player_aces, dealer_sum, dealer_aces)
            print(rec_action)
            return render_template('result.html', max_expected_value=max_expected_value,
                                   max_odds_winning=max_odds_winning, max_bribe_count=max_bribe_count,
                                   player_sum=player_sum, player_aces=player_aces,
                                   dealer_sum=dealer_sum, dealer_aces=dealer_aces, rec_action=rec_action)
        except ValueError:
            return render_template('result.html', error="Invalid input. Please enter valid card values.")
    return render_template('index.html', player_sum=player_sum, player_aces=player_aces, dealer_sum=dealer_sum, dealer_aces=dealer_aces)

if __name__ == '__main__':
    app.run(debug=True)
