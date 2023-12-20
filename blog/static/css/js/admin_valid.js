(function ($) {
    $(document).ready(function () {
        // Custom form validation
        function validateArticleForm() {
            var title = $('#id_title').val();
            var content = $('#id_content').val();

            
            if (!title.trim()) {
                alert('Title cannot be empty.');
                return false;
            }

            if (content.length < 50) {
                alert('Post content should be at least 50 characters long.');
                return false;
            }

            return true;  // Form is valid
        }

        // Attach custom validation to the save button
        $('#article_form').submit(function () {
            return validateArticleForm();
        });
    });
})(django.jQuery);
