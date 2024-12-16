document.addEventListener('DOMContentLoaded', function() {
    const faqItems = document.querySelectorAll('.faq-item h2');

    faqItems.forEach(function(item) {
        item.addEventListener('click', function() {
            const p = item.nextElementSibling;
            p.style.display = p.style.display === 'none' ? 'block' : 'none';
        });
    });
});
