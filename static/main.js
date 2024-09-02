// main.js

document.getElementById('connect-button').addEventListener('click', function() {
    const username = prompt("Please enter your username:");
    if (username) {
        document.getElementById('player-connect').innerHTML = `<p>🔑 Logged in as: ${username}</p>`;
        
        // Enable the "Start Game" button once the user has logged in
        document.getElementById('start-game-button').removeAttribute('disabled');
    }
});

document.getElementById('start-game-button').addEventListener('click', async function() {
    const gameModule = await import('./game.js');
    gameModule.startGame();
});

document.getElementById('new-game-button').addEventListener('click', async function() {
    const gameModule = await import('./game.js');
    gameModule.newGame();
});

document.getElementById('theme-toggle-button').addEventListener('click', async function() {
    const themeModule = await import('./theme.js');
    themeModule.toggleTheme();
});
