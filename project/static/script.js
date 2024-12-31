document.addEventListener("DOMContentLoaded", () => {
    // Comutare între calculatoare
    const toggleCalculator = (type) => {
        const simpleCalculator = document.getElementById("simple-calculator");
        const advancedCalculator = document.getElementById("advanced-calculator");

        if (type === "advanced") {
            simpleCalculator.style.display = "none";
            advancedCalculator.style.display = "block";
        } else {
            simpleCalculator.style.display = "block";
            advancedCalculator.style.display = "none";
        }
    };

    // Adaugă evenimente la butoane
    document.querySelectorAll("button").forEach((button) => {
        button.addEventListener("mouseenter", () => {
            button.style.transform = "scale(1.05)";
        });
        button.addEventListener("mouseleave", () => {
            button.style.transform = "scale(1)";
        });
    });

    window.toggleCalculator = toggleCalculator; // Pentru acces global
});
function toggleCalculator(type) {
    if (type === 'advanced') {
        document.getElementById('simple-calculator').style.display = 'none';
        document.getElementById('advanced-calculator').style.display = 'block';
    } else {
        document.getElementById('simple-calculator').style.display = 'block';
        document.getElementById('advanced-calculator').style.display = 'none';
    }
}

