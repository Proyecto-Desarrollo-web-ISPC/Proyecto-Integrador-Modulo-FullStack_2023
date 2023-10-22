
export function validateFields() {
    const inputNombre = document.getElementById("inputNombre");
    const inputApellido = document.getElementById("inputApellido");
    const inputEmail = document.getElementById("inputEmail");
    const inputMensaje = document.getElementById("inputMensaje");
    const form = document.querySelector("#contactForm");
    const confirmationMessage = document.getElementById("confirmationMessage");
    const submitButton = document.querySelector("#buttonContacto");

    function checkFormValidation() {
        if(!form.checkValidity()){
            submitButton.disabled = true;
        } else {
            submitButton.disabled = false;   
        }; 
    };

    function isValidEmail(email) {
        return email.includes('@') || email.includes('.');
    };

    function validateField(input, validator) {
        const value = input.value.trim();
        if (validator(value)) {
            input.classList.remove("is-invalid");                   
            input.classList.add("is-valid");
            checkFormValidation();
        } else {
            input.classList.remove("is-valid");
            input.classList.add("is-invalid");
            checkFormValidation();
        };
    };


    inputNombre.addEventListener("input", function() {          
        validateField(inputNombre, value => value !== "");
    });

    inputApellido.addEventListener("input", function() {
        validateField(inputApellido, value => value !== "");
    });

    inputEmail.addEventListener("input", function() {
        validateField(inputEmail, isValidEmail);
    });

    inputMensaje.addEventListener("input", function() {
        validateField(inputMensaje, value => value !== "");
    });

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        if (form.checkValidity()) {
            // Mostrar el mensaje de confirmación de envío
            confirmationMessage.style.display = "block";
            // Deshabilitar los campos del formulario
            inputNombre.disabled = true;
            inputApellido.disabled = true;
            inputEmail.disabled = true;
            inputMensaje.disabled = true;

        // Deshabilitar el botón de envío
            submitButton.disabled = true;
            checkFormValidation();
        };
    });
};