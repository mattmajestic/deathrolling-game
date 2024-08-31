let intervalId;
let roundCounter = 1;
let player1Roll = null;
let player2Roll = null;

function startGame() {
    const wager_amount = document.getElementById('wager_amount').value;

    fetch('/start_game', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ wager_amount: wager_amount })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('start-game').style.display = 'none';
        document.getElementById('game-info').style.display = 'block';
        document.getElementById('current-roll').innerText = `Current Roll: ${data.current_roll}`;
        document.getElementById('status').innerText = data.status;
        document.getElementById('roll-list').innerHTML = '';  // Clear previous rolls
        roundCounter = 1;

        // Start the automatic rolling every 2 seconds
        intervalId = setInterval(rollDice, 2000);
    });
}

function rollDice() {
    fetch('/roll_dice', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('current-roll').innerText = `Current Roll: ${data.current_roll}`;
        document.getElementById('status').innerText = data.status;

        if (roundCounter % 2 !== 0) {
            // Player 1's turn
            player1Roll = data.current_roll;
        } else {
            // Player 2's turn
            player2Roll = data.current_roll;

            // Now both players have rolled, so we add the row
            const rollList = document.getElementById('roll-list');
            const row = document.createElement('tr');

            const roundCell = document.createElement('td');
            roundCell.className = 'round';
            roundCell.innerText = `Round ${Math.floor(roundCounter / 2) + 1}`;

            const player1RollCell = document.createElement('td');
            player1RollCell.className = 'player-roll';
            player1RollCell.innerText = player1Roll;

            const player2RollCell = document.createElement('td');
            player2RollCell.className = 'player-roll';
            player2RollCell.innerText = player2Roll;

            row.appendChild(roundCell);
            row.appendChild(player1RollCell);
            row.appendChild(player2RollCell);

            rollList.appendChild(row);

            // Reset for the next round
            player1Roll = null;
            player2Roll = null;
        }

        roundCounter++;

        if (data.game_over) {
            document.getElementById('status').innerText = `Game Over! ${data.winner} wins!`;

            // Stop the automatic rolling
            clearInterval(intervalId);

            // Trigger confetti when someone wins
            confetti();
        }
    });
}

function confetti() {
    confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
    });
}
