from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/rankings')
def rankings():
    # This is just a simplified example. Ideally, you'll load the rankings 
    # from your earlier repository setup or from some database.
    players = [
        {"name": "Player A", "pos": "QB", "age": 25},
        {"name": "Player B", "pos": "RB", "age": 27},
        # Add more players...
    ]
    return render_template('rankings.html', players=players)
if __name__ == '__main__':
    app.run(debug=True)