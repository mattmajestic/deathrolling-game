// ui.js
export function toggleTheme() {
    document.body.classList.toggle('light-mode');
    if (document.body.classList.contains('light-mode')) {
        document.getElementById('theme-toggle-button').innerHTML = '🌞 Mode'; // Switch to Sun emoji for light mode
    } else {
        document.getElementById('theme-toggle-button').innerHTML = '💀 Mode'; // Switch to Skull emoji for dark mode
    }
}

export function connectPlayer() {
    const username = prompt("Please enter your username:");
    if (username) {
        document.getElementById('player-connect').innerHTML = `<p>Connected as: ${username}</p>`;
    }
}

export function openModal() {
    document.getElementById('usernameModal').style.display = 'flex';
}

export function closeModal() {
    document.getElementById('usernameModal').style.display = 'none';
}

export function submitUsername() {
    const username = document.getElementById('username-input').value;
    if (username) {
        document.getElementById('player-connect').innerHTML = `<p>Connected as: ${username}</p>`;
        closeModal();
    }
}
