import { loginPasswordVisibility, registerPasswordVisibility } from "./passwordHider.js";
import { getUserDataLogin, getUserDataRegister } from "./registerLoginUsers.js";

export let isUserLoggedIn = {
    connectSession: JSON.parse(localStorage.getItem('isUserLoggedIn')) || false
};

export function initSystem(){
    const formStructure = {
        loginForm: document.getElementById('loginForm'), 
        loginButton: loginForm.querySelector('#logBtn'),

        registerForm: document.getElementById('registerForm'),
        registerButton: registerForm.querySelector('#registerBtn'),
        
        submitRegisterBtn: registerForm.querySelector('#submitRegisterBtn'),
        submitLoginBtn: loginForm.querySelector('#submitLoginBtn'),
        
        loginNavBtn: document.getElementById('loginBtn')
    }
    loginPasswordVisibility();
    registerPasswordVisibility();
    getUserDataLogin(formStructure, isUserLoggedIn);
    getUserDataRegister(formStructure, isUserLoggedIn);
};