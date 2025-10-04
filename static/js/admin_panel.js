document.addEventListener('DOMContentLoaded', function () {
    const dropdowns = document.querySelectorAll('.sidebar-dropdown > a');

    dropdowns.forEach(drop => {
        drop.addEventListener('click', function () {
            const parent = this.parentElement;
            const menu = this.nextElementSibling;

            // بستن همه زیرمنوها به جز این
            document.querySelectorAll('.sidebar-dropdown').forEach(d => {
                if (d !== parent) d.classList.remove('active');
            });

            // باز/بسته کردن این زیرمنو
            parent.classList.toggle('active');
        });
    });
});
