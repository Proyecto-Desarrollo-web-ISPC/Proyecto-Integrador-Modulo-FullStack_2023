import { basicStructure, setDarkMode, setLightMode } from "./themeModeCart"
setDarkMode();
setLightMode();


const structureProductsSection = {
    addToCartBtn: document.getElementsByClassName("addProductBtn"),
    card: document.getElementsByClassName("card"),
    modalCardContainer: document.getElementsByClassName("modalCardContainer"), 
    modalTitle: document.getElementsByClassName("modalTitle"),
    productCard: document.getElementsByClassName("productCard")
}

const changeMode = {
    setProductsDarkMode: function(){
        basicStructure.togglerBtnDM.addEventListener("click", () => {
            for(let i = 0; i < structureProductsSection.card.length; i++){
                structureProductsSection.card[i].setAttribute("data-bs-theme", "dark");
            };
            for(let i = 0; i < structureProductsSection.modalCardContainer.length; i++){
                structureProductsSection.modalCardContainer[i].setAttribute("data-bs-theme", "dark");
            };
            for(let i = 0; i < structureProductsSection.modalTitle.length; i++){
                structureProductsSection.modalTitle[i].style.color = "#f5f5f5";
            };
        })
    },
    setProductsLightMode: basicStructure.togglerBtnLM.addEventListener("click", () => {

    }),
}
