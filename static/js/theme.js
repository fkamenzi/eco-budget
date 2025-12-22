const root = document.documentElement;
const btn = document.getElementById("theme-btn");

// Load saved theme
const savedTheme = localStorage.getItem("theme") || "light";
root.setAttribute("data-theme", savedTheme);
btn.textContent = savedTheme === "dark" ? "☀️" : "🌙";

// Toggle theme
btn.addEventListener("click", () => {
    const current = root.getAttribute("data-theme");
    const next = current === "light" ? "dark" : "light";

    root.setAttribute("data-theme", next);
    localStorage.setItem("theme", next);

    btn.textContent = next === "dark" ? "☀️" : "🌙";
});
