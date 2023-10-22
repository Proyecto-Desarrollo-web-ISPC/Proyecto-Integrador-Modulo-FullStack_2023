import { buildUser } from "./buildUserIntances.js";
import { getUsersLocalStoraged } from "./handleUsersLs.js";

function generateUniqueUserId(users) {
    //* Find the highest ID among existing users and add 1
    const maxId = users.reduce((max, user) => Math.max(max, user.id || 0), 0);
    return maxId + 1;
};

export function getUserDataRegister(formStructure, isUserLoggedIn){
    formStructure.registerButton.addEventListener('click', (e) => {
        e.preventDefault();
        const formData = {
            name: formStructure.registerForm.querySelector('#inputRegisterFullName').value,
            lastName: formStructure.registerForm.querySelector('#inputRegisterLastName').value,
            dni: formStructure.registerForm.querySelector('#inputRegisterDNI').value,
            domicilio: formStructure.registerForm.querySelector('#inputRegisterDomicilio').value,
            email: formStructure.registerForm.querySelector('#inputRegisterEmail').value,
            password: formStructure.registerForm.querySelector('#inputRegisterPassword').value,
        };
        const usersRegistered = getUsersLocalStoraged();
        const isUserRegistered = usersRegistered.some(user => user.email === formData.email);
        
        if (isUserRegistered === true) {
            alert('¡Usuario ya registrado!')
        } else if ((!String(formData.email).includes('@')) || (!String(formData.email).includes('.'))){
            alert('¡Tu usuario debe incluir @ y la correspondiente extensión con punto (.com/.net/.ar/.io), según corresponda!')
        } else {
            formData.id = generateUniqueUserId(usersRegistered);
            buildUser(formData);
            if(Boolean(isUserLoggedIn.connectSession) === false){
                let isClientConnected = isUserLoggedIn.connectSession
                isClientConnected = true;
                localStorage.setItem('isUserLoggedIn', JSON.stringify(isClientConnected));
            };
            alert('¡Bienvenido/a!')
            
            formStructure.submitRegisterBtn.click();

            setTimeout(() =>{
                window.location.reload();
            }, 3000);
        };
    });
};

export function getUserDataLogin(formStructure, isUserLoggedIn){
    formStructure.loginButton.addEventListener('click', (e) => {
        e.preventDefault();
        const formData = {
            email: formStructure.loginForm.querySelector('#inputLoginEmail').value,
            password: formStructure.loginForm.querySelector('#inputPassword').value 
        };

        const usersRegistered = getUsersLocalStoraged();
        const user = usersRegistered.find(u => u.email === formData.email);
        if (user && user.password === formData.password) {
            
            if(Boolean(isUserLoggedIn.connectSession) === false){
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