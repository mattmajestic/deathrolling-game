// theme.js

export function toggleTheme() {
    document.body.classList.toggle('light-mode');
    const button = document.getElementById('theme-toggle-button');
    if (document.body.classList.contains('light-mode')) {
        button.innerHTML = '🌞 Mode'; // Switch to Sun emoji for light mode
    } else {
        button.innerHTML = '💀 Mode'; // Switch to Skull emoji for dark mode
    }
}
