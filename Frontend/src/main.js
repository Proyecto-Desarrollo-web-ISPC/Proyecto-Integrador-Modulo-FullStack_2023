import { basicStructure, toggleMode } from './themeModeToggler.js' 
import { validateFields } from './validadores/validator.js';
import { validateForms } from './validadores/register.js';

const path = String(location.href);

if(path.includes('about.html')){
    document.addEventListener("DOMContentLoaded", validateFields());
};

// Ejecución de modos de tema
setDarkMode();
function setDarkMode(){
    basicStructure.togglerBtnDM.addEventListener("click", () => {
        toggleMode.darkMode();
    });
}

setLightMode();
function setLightMode(){
    basicStructure.togglerBtnLM.addEventListener("click", () => {
        toggleMode.lightMode();
    })
};

document.addEventListener("DOMContentLoaded", validateForms());