document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.button');
    buttons.forEach(button => {
        button.addEventListener('mouseover', () => button.style.opacity = '0.95');
        button.addEventListener('mouseout', () => button.style.opacity = '1');
    });
});
