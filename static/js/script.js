// document.addEventListener("DOMContentLoaded", function() {
//     window.addEventListener("load", function() {
//         // Artificial delay (in milliseconds)
//         const delay = 3000;
//         setTimeout(function() {
//             document.body.classList.add('loaded');
//         }, delay);
//     });
// });
document.addEventListener("DOMContentLoaded", function () {
    // Hide preloader after 3 seconds
    setTimeout(function () {
        document.body.classList.add("loaded");
    }, 3000);

    // Image Preview Function
    function previewImage(event) {
        const input = event.target;
        const preview = document.getElementById("imagePreview");
        const previewImg = document.getElementById("previewImg");

        if (input.files && input.files[0]) {
            const reader = new FileReader();
            reader.onload = function (e) {
                previewImg.src = e.target.result;
                preview.style.display = "block";
            };
            reader.readAsDataURL(input.files[0]);
        } else {
            preview.style.display = "none";
        }
    }

    // Attach event listener for file input
    const uploadBtn = document.getElementById("uploadBtn");
    if (uploadBtn) {
        uploadBtn.addEventListener("change", previewImage);
    }
});
