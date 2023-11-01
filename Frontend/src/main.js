import { basicStructure, toggleTheme } from './themeModeToggler.js' 
import { validateFields } from './validadores/validator.js';
import { initSystem } from './GestorDeUsuarios/getUserInfo.js'
import { checkLoginStatus } from './GestorDeUsuarios/handleLoginLogOutinterface.js';
import { isUserLoggedIn } from './GestorDeUsuarios/getUserInfo.js';
import { getUsersLocalStoraged } from './GestorDeUsuarios/handleUsersLs.js';
import { logOutUser } from './GestorDeUsuarios/handleLoginLogOutinterface.js';
import { disableAddButtons } from './GestorDeUsuarios/registerLoginUsers.js';

// Ejecución de validadores
const path = String(location.href);
if(path.includes('about.html')){
    document.addEventListener("DOMContentLoaded", validateFields());
};


// Ejecución de modos de tema
basicStructure.togglerBtnDM.addEventListener("click", () => {
    toggleTheme('dark');
});

basicStructure.togglerBtnLM.addEventListener("click", () => {
    toggleTheme('light');
})

// Ejecución de gestor de usuarios
document.addEventListener('DOMContentLoaded', loadEvents());
function loadEvents(){
    if(path.includes('products.html')){
        disableAddButtons()
    };
    initSystem();
    checkLoginStatus(isUserLoggedIn);
    getUsersLocalStoraged();
    const logoutBtn = document.querySelector('#endClientSession');
    logoutBtn.addEventListener('click', () => logOutUser(isUserLoggedIn));
}