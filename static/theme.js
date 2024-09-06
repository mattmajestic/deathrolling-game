// theme.js

// Function to toggle between light and dark modes
export function toggleTheme() {
    document.body.classList.toggle('light-mode');
    const button = document.getElementById('theme-toggle-button');

    if (document.body.classList.contains('light-mode')) {
        button.innerHTML = '🌞 Mode'; // Switch to Sun emoji for light mode
        localStorage.setItem('theme', 'light'); // Save theme to localStorage
    } else {
        button.innerHTML = '💀 Mode'; // Switch to Skull emoji for dark mode
        localStorage.setItem('theme', 'dark'); // Save theme to localStorage
    }
}

// Function to load the theme from localStorage when the page loads
export function loadTheme() {
    const savedTheme = localStorage.getItem('theme');
    const button = document.getElementById('theme-toggle-button');

    if (savedTheme === 'light') {
        document.body.classList.add('light-mode');
        button.innerHTML = '🌞 Mode'; // Set button for light mode
    } else {
        document.body.classList.remove('light-mode'); // Default to dark mode
        button.innerHTML = '💀 Mode'; // Set button for dark mode
    }
}
