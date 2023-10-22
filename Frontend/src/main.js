import { basicStructure, toggleMode } from './themeModeToggler.js' 
import { validateFields } from './validadores/validator.js';
import { validateForms } from './validadores/register.js';

const path = String(location.href);

if(path.includes('about.html')){
    document.addEventListener("DOMContentLoaded", validateFields());
};

document.addEventListener("DOMContentLoaded", validateForms());

// Ejecución de modos de tema
basicStructure.togglerBtnDM.addEventListener("click", () => {
    toggleTheme('dark');
});

basicStructure.togglerBtnLM.addEventListener("click", () => {
    toggleTheme('light');
})