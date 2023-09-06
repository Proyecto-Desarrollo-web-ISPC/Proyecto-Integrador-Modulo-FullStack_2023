import { basicStructure, setDarkMode, setLightMode } from "./themeModeCart";

basicStructure.togglerBtnDM.addEventListener("click", () => {
    setDarkMode()
})
basicStructure.togglerBtnLM.addEventListener("click", () => {
    setLightMode()
})