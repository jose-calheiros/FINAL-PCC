document.addEventListener('DOMContentLoaded', function () {
    const tabs = document.querySelectorAll('.tab-link');
    const contents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', function () {
            const tabId = this.getAttribute('data-tab');

            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active'));
            // Hide all tab contents
            contents.forEach(c => c.classList.remove('active'));

            // Add active class to clicked tab
            this.classList.add('active');
            // Show the corresponding tab content
            document.getElementById(tabId).classList.add('active');
        });
    });
});