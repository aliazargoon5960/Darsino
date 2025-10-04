// باز و بسته کردن dropdown های سایدبار
document.addEventListener('DOMContentLoaded', function () {
    const dropdowns = document.querySelectorAll('.sidebar-dropdown > a');

    dropdowns.forEach(drop => {
        drop.addEventListener('click', function () {
            const menu = this.nextElementSibling;
            if (menu.style.display === "block") {
                menu.style.display = "none";
            } else {
                // همه منوهای باز را ببند
                document.querySelectorAll('.sidebar-dropdown-menu').forEach(m => m.style.display = "none");
                menu.style.display = "block";
            }
        });
    });
});
