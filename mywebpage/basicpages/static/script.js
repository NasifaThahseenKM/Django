document.addEventListener("DOMContentLoaded", function() {
    const button = document.getElementById("greet-btn");
    if (button) {
        button.addEventListener("click", function() {
            alert("Hello! Thanks for visiting my page!");
        });
    }
});
