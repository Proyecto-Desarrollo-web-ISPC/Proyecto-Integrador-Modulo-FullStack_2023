import {basicStructure, toggleMode} from './themeModeToggler.js' 

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
}