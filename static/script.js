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
        document.getElementById('new-game-button').style.display = 'none'; // Hide new game button
        document.getElementById('current-roll').innerText = `Current Roll: ${data.current_roll}`;
        document.getElementById('status').innerText = data.status;
        document.getElementById('roll-list').innerHTML = '';  // Clear previous rolls
        roundCounter = 1;

        // Start the rolling process with Player 1
        player1Roll = data.current_roll;
        intervalId = setTimeout(() => rollDice(), 1000);
    });
}

function rollDice() {
    fetch('/roll_dice', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (roundCounter % 2 !== 0) {
            // Player 1's turn
            player1Roll = data.current_roll;
            updateTable(); // Update after Player 1's roll
        } else {
            // Player 2's turn
            player2Roll = data.current_roll;
            updateTable(); // Update after Player 2's roll
        }

        document.getElementById('current-roll').innerText = `Current Roll: ${data.current_roll}`;
        document.getElementById('status').innerText = data.status;

        if (data.game_over) {
            document.getElementById('status').innerText = `Game Over! ${data.winner} wins!`;

            // Stop the automatic rolling
            clearTimeout(intervalId);

            // Show the new game button
            document.getElementById('new-game-button').style.display = 'block';

            // Trigger confetti when someone wins
            confetti();
        } else {
            // Continue rolling for the next player after 1 second
            intervalId = setTimeout(() => rollDice(), 1000);
            roundCounter++;
        }
    });
}

function updateTable() {
    if (player1Roll !== null && player2Roll !== null) {
        const rollList = document.getElementById('roll-list');
        const row = document.createElement('tr');

        const roundCell = document.createElement('td');
        roundCell.className = 'round';
        roundCell.innerText = `Round ${Math.ceil(roundCounter / 2)}`;

        const player1RollCell = document.createElement('td');
        player1RollCell.className = 'player-roll';
        player1RollCell.innerText = player1Roll !== null ? player1Roll : '-';

        const player2RollCell = document.createElement('td');
        player2RollCell.className = 'player-roll';
        player2RollCell.innerText = player2Roll !== null ? player2Roll : '-';

        row.appendChild(roundCell);
        row.appendChild(player1RollCell);
        row.appendChild(player2RollCell);

        rollList.appendChild(row);

        // Reset rolls for the next round
        player1Roll = null;
        player2Roll = null;
    }
}

function confetti() {
    confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
    });
}

function newGame() {
    // Reset the UI for a new game
    document.getElementById('start-game').style.display = 'block';
    document.getElementById('game-info').style.display = 'none';
    document.getElementById('new-game-button').style.display = 'none';
    roundCounter = 1;
    player1Roll = null;
    player2Roll = null;
}
