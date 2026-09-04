// ======= Mobile Menu Toggle =======
function toggleMenu() {
    const nav = document.getElementById('navLinks');
    const btn = document.getElementById('mobileMenuBtn');
    const isOpen = nav.classList.toggle('mobile-open');
    btn.innerHTML = isOpen
        ? '<i class="fa-solid fa-xmark"></i>'
        : '<i class="fa-solid fa-bars"></i>';
}

// Close menu if clicked outside
document.addEventListener('click', function (e) {
    const nav = document.getElementById('navLinks');
    const btn = document.getElementById('mobileMenuBtn');
    if (nav && btn && !nav.contains(e.target) && !btn.contains(e.target)) {
        nav.classList.remove('mobile-open');
        btn.innerHTML = '<i class="fa-solid fa-bars"></i>';
    }
});


// ======= Image Preview on Upload =======
function previewImage(event) {
    const input = event.target;
    const preview = document.getElementById('imagePreview');
    const uploadContent = document.getElementById('uploadContent');

    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
            if (uploadContent) {
                uploadContent.style.display = 'none';
            }
        };
        reader.readAsDataURL(input.files[0]);
    }
}


// ======= Password Visibility Toggle =======
function togglePasswordVisibility(inputId, btn) {
    const input = document.getElementById(inputId);
    if (!input) return;
    const isText = input.type === 'text';
    input.type = isText ? 'password' : 'text';
    btn.innerHTML = isText
        ? '<i class="fa-regular fa-eye"></i>'
        : '<i class="fa-regular fa-eye-slash"></i>';
}

// Legacy support
function LoginshowPassword() {
    togglePasswordVisibility('loginpassword', document.querySelector('.show-pass-btn'));
}


// ======= Auto-dismiss flash alerts =======
(function () {
    const alert = document.getElementById('flashAlert');
    if (alert) {
        setTimeout(function () {
            alert.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(30px)';
            setTimeout(() => alert.remove(), 500);
        }, 4000);
    }
})();


// ======= FAQ Accordion =======
function toggleFaq(btn) {
    const item = btn.closest('.faq-item');
    const answer = item.querySelector('.faq-answer');
    const icon = btn.querySelector('i');
    const isOpen = item.classList.toggle('faq-open');

    if (isOpen) {
        answer.style.maxHeight = answer.scrollHeight + 'px';
        icon.style.transform = 'rotate(180deg)';
    } else {
        answer.style.maxHeight = '0';
        icon.style.transform = 'rotate(0deg)';
    }

    // Close other open FAQs
    document.querySelectorAll('.faq-item.faq-open').forEach(function (openItem) {
        if (openItem !== item) {
            openItem.classList.remove('faq-open');
            openItem.querySelector('.faq-answer').style.maxHeight = '0';
            openItem.querySelector('.faq-question i').style.transform = 'rotate(0deg)';
        }
    });
}


// ======= Scroll-based Navbar Shadow =======
window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        navbar.style.boxShadow = window.scrollY > 10
            ? '0 4px 20px rgba(15,23,42,0.08)'
            : 'none';
    }
});


// ======= Animate elements on scroll (Intersection Observer) =======
(function () {
    const targets = document.querySelectorAll('.item-card, .service-card, .value-card, .step, .stat');
    if (!targets.length) return;

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    targets.forEach(function (el) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(el);
    });
})();
