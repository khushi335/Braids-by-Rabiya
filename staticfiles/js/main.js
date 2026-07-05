document.querySelectorAll('.accordion-trigger-bar').forEach(trigger => {
    trigger.addEventListener('click', () => {
        const parent = trigger.parentElement;
        
        // Toggle the target panel active state cleanly
        if (parent.classList.contains('active')) {
            parent.classList.remove('active');
        } else {
            // Optional structural layout wash: closes other fields sequentially
            document.querySelectorAll('.intel-accordion-block').forEach(item => item.classList.remove('active'));
            parent.classList.add('active');
        }
    });
});