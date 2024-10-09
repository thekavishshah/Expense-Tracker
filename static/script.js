document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            if (!confirm("Are you sure you want to delete this expense?")) {
                event.preventDefault();
            }
        });
    });
});
