const redirectToEdit = (elem) => {
    window.location.href = elem.getAttribute('data-edit-url');
};

const confirmDelete = (event) => {
    event.stopPropagation();
    if (!confirm('Удалить?')) {
        event.preventDefault();
    }
};