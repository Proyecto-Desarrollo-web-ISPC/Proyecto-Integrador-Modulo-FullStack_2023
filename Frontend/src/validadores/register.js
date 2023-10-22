export function validateForms() {
    const form = document.getElementById("regForm");
    const dniInput = form.querySelector("#inputRegisterDNI");
    const passwordInput = form.querySelector("#inputRegisterPassword");
    const confirmPasswordInput = form.querySelector("#inputRegisterConfirmPassword");
    const successMessage = form.querySelector("#successMessage");
    
    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita el envío automático del formulario
        // console.log(event.target) - Se consolea el elemento que recibe el evento (click por default)

        // Valida el DNI
        const dniValue = dniInput.value;
        if (!validateDNI(dniValue)) {
            alert("DNI inválido. Debe estar entre 1000000 y 99999999.");
            event.preventDefault();
            return;
        };

        // Valida que las contraseñas coincidan
        const passwordValue = passwordInput.value;
        const confirmPasswordValue = confirmPasswordInput.value;
        if (passwordValue !== confirmPasswordValue) {
            alert("Las contraseñas no coinciden.");
            event.preventDefault();
            return;
        };

        // Valida la contraseña
        if (!validatePassword(passwordValue)) {
            alert("La contraseña debe tener al menos 8 caracteres y contener números, letras mayúsculas, letras minúsculas y símbolos.");
            event.preventDefault();
            return;
        };

        successMessage.style.display = "block";

        setTimeout(function() {
            successMessage.style.display = "none"; // Oculta el mensaje de envio
            form.submit(); // Se envia manualmente el formulario si se validan todos los datos
        }, 3000);
    });

    // Funcion para Validar el DNI
    function validateDNI(dni) {
        const dniNumber = parseInt(dni);
        return dniNumber >= 1000000 && dniNumber <= 99999999;
    };

    // Funcion para Validar que la contraseña contenga mayusculas, minusculas, caracteres especiales y numeros
    function validatePassword(password) {
        const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$/;
        return passwordRegex.test(password);
    };
};

