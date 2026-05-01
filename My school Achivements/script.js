// script.js - Portfolio Interactivity

// 1. Project Buttons - Show Alert
document.getElementById("projects").onclick = function (e) {
    if (e.target.dataset.proj) {
        let box = document.getElementById("projectAlert");
        box.textContent = "You clicked: " + e.target.dataset.proj + " ✅";
        box.classList.remove("d-none");
        setTimeout(() => box.classList.add("d-none"), 3000);
    }
};

// 2. Contact Form - Send with Formspree
document.getElementById("contactForm").onsubmit = function (e) {
    e.preventDefault(); // Prevent default form submission
    let form = this;

    fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" }
    })
        .then(res => {
            if (res.ok) {
                document.getElementById("sentOk").classList.remove("d-none");
                form.reset(); // Clear form after success
            } else {
                document.getElementById("sentFail").classList.remove("d-none");
            }
        })
        .catch(() => {
            document.getElementById("sentFail").classList.remove("d-none");
        });
};

// 3. Smooth Scroll for Navbar Links
document.querySelectorAll('a.nav-link').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href'))
            .scrollIntoView({ behavior: 'smooth' });
    });
});
