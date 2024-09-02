// modal.js

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
