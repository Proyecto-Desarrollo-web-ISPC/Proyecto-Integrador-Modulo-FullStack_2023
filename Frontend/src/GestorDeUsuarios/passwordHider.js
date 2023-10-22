export function loginPasswordVisibility(){
    const loginPasswordInput = document.getElementById('inputPassword');
    const loginVisibilityOn = document.getElementById('loginVisibilityOn');
    const loginVisibilityOff = document.getElementById('loginVisibilityOff');

        loginVisibilityOn.style.cursor = 'pointer';
        loginVisibilityOff.style.cursor = 'pointer';
    
        loginVisibilityOn.addEventListener("click", () => {
            toggleLoginPasswordVisibility();
        });
    
        loginVisibilityOff.addEventListener("click", () => {
            toggleLoginPasswordVisibility();
        });
    
        function toggleLoginPasswordVisibility() {
            if (loginPasswordInput.type === "password") {
                loginPasswordInput.type = "text";
                loginVisibilityOn.classList.add('d-none');
                loginVisibilityOn.classList.remove('d-block');
    
                loginVisibilityOff.classList.add('d-block');
                loginVisibilityOff.classList.remove('d-none')
            } else {
                loginPasswordInput.type = "password";
                loginVisibilityOn.classList.add('d-block');
                loginVisibilityOn.classList.remove('d-none');
    
                loginVisibilityOff.classList.add('d-none');
                loginVisibilityOff.classList.remove('d-block')
            };
        };
};

export function registerPasswordVisibility(){
    const registerPasswordInput = document.getElementById('inputRegisterPassword')
    const registerVisibilityOn = document.getElementById('registerVisibilityOn');
    const registerVisibilityOff = document.getElementById('registerVisibilityOff');
    const confirmPasswordInput = document.getElementById('inputRegisterConfirmPassword')

    registerVisibilityOn.style.cursor = 'pointer';
    registerVisibilityOff.style.cursor = 'pointer';
    
    registerVisibilityOn.addEventListener("click", () => {
        toggleLoginPasswordVisibility();
    });
    
    registerVisibilityOff.addEventListener("click", () => {
        toggleLoginPasswordVisibility();
    });
    
    function toggleLoginPasswordVisibility() {
        if (registerPasswordInput.type === "password") {
            registerPasswordInput.type = "text";
            confirmPasswordInput.type = "text"
            registerVisibilityOn.classList.add('d-none');
            registerVisibilityOn.classList.remove('d-block');
            registerVisibilityOff.classList.add('d-block');
            registerVisibilityOff.classList.remove('d-none')
        } else {
            registerPasswordInput.type = "password";
            confirmPasswordInput.type = "password"
            registerVisibilityOn.classList.add('d-block');
            registerVisibilityOn.classList.remove('d-none');
            registerVisibilityOff.classList.add('d-none');
            registerVisibilityOff.classList.remove('d-block')
        };
    };
};