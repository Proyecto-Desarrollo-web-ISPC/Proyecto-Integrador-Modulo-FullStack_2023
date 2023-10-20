import {basicStructure, toggleTheme} from './themeModeToggler.js' 

// Ejecución de modos de tema
basicStructure.togglerBtnDM.addEventListener("click", () => {
    toggleTheme('dark');
});

basicStructure.togglerBtnLM.addEventListener("click", () => {
    toggleTheme('light');
})