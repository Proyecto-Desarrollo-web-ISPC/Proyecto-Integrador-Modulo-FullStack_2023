import { basicStructure, setDarkMode, setLightMode } from "./themeModeCart"

const structureProductsSection = {
    addToCartBtn: document.getElementsByClassName("addProductBtn"),
    productCard: document.getElementsByClassName("productCard"),
    modalArgentina: document.getElementById("modalArgentina"), 
    modalBrasil: document.getElementById("modalBrasil"),
    modalAlemania: document.getElementById("modalAlemania"),
    modalEspana: document.getElementById("modalEspana"),
    modalItalia: document.getElementById("modalItalia"),
    modalFrancia: document.getElementById("modalFrancia"),
    modalInglaterra: document.getElementById("modalInglaterra"),
    modalUruguay: document.getElementById("modalUruguay"), 
    modalTitle: document.getElementsByClassName("modalTitle"),
    cardContainer: document.getElementsByClassName("cardContainer")
}

const changeMode = {
    setProductsLightMode: function(){
        for(let i = 0; i < structureProductsSection.productCard.length; i++){
            structureProductsSection.productCard[i].setAttribute("data-bs-theme", "light");
        };
        for(let i = 0; i < basicStructure.modalTitle.length; i++){
            structureProductsSection.modalTitle[i].style.color = "#222222";
        };
        structureProductsSection.modalArgentina.dataset.bsTheme = "light";
        structureProductsSection.modalBrasil.dataset.bsTheme = "light";
        structureProductsSection.modalEspana.dataset.bsTheme = "light";
        structureProductsSection.modalItalia.dataset.bsTheme = "light";
        structureProductsSection.modalFrancia.dataset.bsTheme = "light";
        structureProductsSection.modalInglaterra.dataset.bsTheme = "light";
        structureProductsSection.modalUruguay.dataset.bsTheme = "light";
    },
    setProductsDarkMode: function(){
        for(let i = 0; i < structureProductsSection.productCard.length; i++){
            structureProductsSection.productCard[i].setAttribute("data-bs-theme", "dark");
        };
        for(let i = 0; i < basicStructure.modalTitle.length; i++){
            structureProductsSection.modalTitle[i].style.color = "#222222";
        }
        structureProductsSection.modalArgentina.dataset.bsTheme = "dark";
        structureProductsSection.modalBrasil.dataset.bsTheme = "dark";
        structureProductsSection.modalEspana.dataset.bsTheme = "dark";
        structureProductsSection.modalItalia.dataset.bsTheme = "dark";
        structureProductsSection.modalFrancia.dataset.bsTheme = "dark";
        structureProductsSection.modalInglaterra.dataset.bsTheme = "dark";
        structureProductsSection.modalUruguay.dataset.bsTheme = "dark";
    }
}



//! REVISAR - Es posible agregar una condición para cambiar el color del modal? 
//! if(role == "dialog" && DM/LM == "active")
/* { modal.setAttribute = "data-bs-theme", "dark" }  */

basicStructure.togglerBtnDM.addEventListener("click", () => {
    changeMode.setProductsDarkMode();
    setDarkMode();
})
basicStructure.togglerBtnDM.addEventListener("click", () => {
    changeMode.setProductsLightMode();
    setLightMode();
})


let modalBackdrop = document.getElementsByClassName("modal-backdrop")
console.dir(structureProductsSection.modalArgentina.attributes)
console.dir(structureProductsSection.modalTitle)