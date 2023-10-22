import { buildUser } from "./buildUserIntances.js";
import { getUsersLocalStoraged } from "./handleUsersLs.js";

function generateUniqueUserId(users) {
    //* Find the highest ID among existing users and add 1
    const maxId = users.reduce((max, user) => Math.max(max, user.id || 0), 0);
    return maxId + 1;
};

export function getUserDataRegister(formStructure, isUserLoggedIn) {
    formStructure.registerButton.addEventListener('click', (e) => {
        e.preventDefault();
        const formData = {
            name: formStructure.registerForm.querySelector('#inputRegisterFullName').value,
            lastName: formStructure.registerForm.querySelector('#inputRegisterLastName').value,
            dni: formStructure.registerForm.querySelector('#inputRegisterDNI').value,
            domicilio: formStructure.registerForm.querySelector('#inputRegisterDomicilio').value,
            email: formStructure.registerForm.querySelector('#inputRegisterEmail').value,
            password: formStructure.registerForm.querySelector('#inputRegisterPassword').value,
            confirmPassword: formStructure.registerForm.querySelector('#inputRegisterConfirmPassword').value,
        };
        const usersRegistered = getUsersLocalStoraged();
        const isUserRegistered = usersRegistered.some(user => user.email === formData.email);
        const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$/;

        if (isUserRegistered === true) {
            alert('¡Usuario ya registrado!')
        } else if ((!String(formData.email).includes('@')) || (!String(formData.email).includes('.'))) {
            alert('¡Tu usuario debe incluir @ y la correspondiente extensión con punto (.com/.net/.ar/.io), según corresponda!')
        } else if (formData.dni < 1000000 || formData.dni > 9999999) {
            alert('El DNI debe estar entre 1,000,000 y 9,999,999.');
        } else if (!passwordRegex.test(formData.password)) {
            alert('La contraseña debe tener al menos 8 caracteres y cumplir con los requisitossss.');
        } else if (formData.password !== formData.confirmPassword) {
            alert('Las contraseñas no coinciden.');
        } else {
            formData.id = generateUniqueUserId(usersRegistered);
            buildUser(formData);
            if (Boolean(isUserLoggedIn.connectSession) === false) {
                let isClientConnected = isUserLoggedIn.connectSession
                isClientConnected = true;
                localStorage.setItem('isUserLoggedIn', JSON.stringify(isClientConnected));
            };
            alert('¡Bienvenido/a!')
            successMessage.style.display = "block";

            formStructure.submitRegisterBtn.click();

            setTimeout(() => {
                window.location.reload();
            }, 3000);
        };
    });
};

export function getUserDataLogin(formStructure, isUserLoggedIn) {
    formStructure.loginButton.addEventListener('click', (e) => {
        e.preventDefault();
        const formData = {
            email: formStructure.loginForm.querySelector('#inputLoginEmail').value,
            password: formStructure.loginForm.querySelector('#inputPassword').value
        };

        const usersRegistered = getUsersLocalStoraged();
        const user = usersRegistered.find(u => u.email === formData.email);
        if (user && user.password === formData.password) {

            if (Boolean(isUserLoggedIn.connectSession) === false) {
                let isClientConnected = isUserLoggedIn.connectSession
                isClientConnected = true;
                localStorage.setItem('isUserLoggedIn', JSON.stringify(isClientConnected));
            };

            alert('¡Bienvenido/a!')
            formStructure.submitLoginBtn.click();
        } else {
            alert('¡Correo y/o contraseña incorrectos!');
        };
    });
};