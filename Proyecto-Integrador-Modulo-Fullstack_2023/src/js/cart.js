// Creación de selector de elementos de navegación y estéticos de la estructura del carro
const structure = {
    togglerBtnLM: document.getElementById("togglerBtnLM"),
    togglerBtnDM: document.getElementById("togglerBtnDM"),
    loginBtn: document.getElementById("loginBtn"),
    body: document.getElementById("bodyId"),
    navbar: document.getElementById("navbarId"),
    footer: document.getElementById("footerId"),
    mainTitle: document.getElementById("mainTitle"),
    h2: document.getElementsByTagName("h2"),
    h3: document.getElementsByTagName("h3"),
    h4: document.getElementsByTagName("h4"),
    h5: document.getElementsByTagName("h5"),
    h6: document.getElementsByTagName("h6"),
    logo: document.getElementById("logo"),
    p: document.getElementsByTagName("p"),
    a: document.getElementsByTagName("a"),
    label: document.getElementsByTagName("label"),
    card: document.getElementsByClassName("card"),
    footerItem: document.getElementsByClassName("footerItem"),
    cardContainer: document.getElementById("cardContainer"),
    modal: document.getElementById("staticBackdrop"),
    modalTitle: document.getElementById("staticBackdropLabel")
}

// Creación de objeto para manejo del modo Dark y Light
const toggleMode = {
    lightMode: function(){
        structure.togglerBtnLM.setAttribute("class", "mx-2 navItem d-none");
        structure.togglerBtnDM.setAttribute("class", "mx-2 navItem d-block");
        const colorBodyLightMode = "linear-gradient(120deg, #f5f5f5 10%, #366608 80%)";
        structure.body.style.background = colorBodyLightMode;
        structure.navbar.setAttribute("data-bs-theme", "light");
        structure.modal.setAttribute("data-bs-theme", "light");
        structure.modalTitle.style.color = "#222222";
        structure.footer.style.background = "#f5f5f5";
        structure.mainTitle.style.color = "#222222";
        // structure.logo.src = "imgPath";
        for(let i = 0; i < structure.h2.length; i++){
            structure.h2[i].style.color = "#222222";
        };
        for(let i = 0; i < structure.h3.length; i++){
            structure.h3[i].style.color = "#222222";
        };
        for(let i = 0; i < structure.h4.length; i++){
            structure.h4[i].style.color = "#222222";
        };
        for(let i = 0; i < structure.h5.length; i++){
            structure.h5[i].style.color = "#222222";
        }
        for(let i = 0; i < structure.h6.length; i++){
            structure.h6[i].style.color = "#222222";
        }
        for(let i = 0; i < structure.p.length; i++){
            structure.p[i].style.color = "#222222";
        }
        for(let i = 0; i < structure.a.length; i++){
            structure.a[i].style.color = "#222222";
        }
        for(let i = 0; i < structure.label.length; i++){
            structure.label[i].style.color = "#222222";
        }
        for(let i = 0; i < structure.p.length; i++){
            structure.p[i].style.color = "##222222"
        }
        for(let i = 0; i < structure.card.length; i++){
            structure.card[i].setAttribute("data-bs-theme", "light");
        }
        for(let i = 0; i < structure.footerItem.length; i++){
            structure.footerItem[i].style.color = "#222222";
        }
    },
    darkMode: function(){
        structure.togglerBtnDM.setAttribute("class", "mx-2 navItem d-none");
        structure.togglerBtnLM.setAttribute("class", "mx-2 navItem d-block");
        const colorBodyDarkMode = "linear-gradient(120deg, #222222 10%, #366608 80%)";
        structure.body.style.background = colorBodyDarkMode;
        structure.navbar.setAttribute("data-bs-theme", "dark");
        structure.modal.setAttribute("data-bs-theme", "dark");
        structure.modalTitle.style.color = "#f5f5f5";
        structure.footer.style.background = "#222222";
        structure.mainTitle.style.color = "#f5f5f5";
        // structure.logo.src = "imgPath"               //Agregar path a nuevo logo
        for(let i = 0; i < structure.h2.length; i++){
            structure.h2[i].style.color = "#f5f5f5";
        };
        for(let i = 0; i < structure.h3.length; i++){
            structure.h3[i].style.color = "#f5f5f5";
        };
        for(let i = 0; i < structure.h4.length; i++){
            structure.h4[i].style.color = "#f5f5f5";
        };
        for(let i = 0; i < structure.h5.length; i++){
            structure.h5[i].style.color = "#f5f5f5";
        }
        for(let i = 0; i < structure.h6.length; i++){
            structure.h6[i].style.color = "#f5f5f5";
        }
        for(let i = 0; i < structure.p.length; i++){
            structure.p[i].style.color = "#f5f5f5";
        }
        for(let i = 0; i < structure.a.length; i++){
            structure.a[i].style.color = "#f5f5f5";
        }
        for(let i = 0; i < structure.label.length; i++){
            structure.label[i].style.color = "#f5f5f5";
        }
        for(let i = 0; i < structure.p.length; i++){
            structure.p[i].style.color = "#f5f5f5"
        }
        for(let i = 0; i < structure.card.length; i++){
            structure.card[i].setAttribute("data-bs-theme", "dark");
        }
        for(let i = 0; i < structure.footerItem.length; i++){
            structure.footerItem[i].style.color = "#f5f5f5";
        }
    }
}

// Ejecución de modos de tema
setDarkMode();
function setDarkMode(){
    structure.togglerBtnDM.addEventListener("click", () => {
        toggleMode.darkMode();
    });
}

setLightMode();
function setLightMode(){
    structure.togglerBtnLM.addEventListener("click", () => {
        toggleMode.lightMode();
    })
}


// Estructura de la tarjeta para el resumen del carro

const cardContainer = document.getElementById("cardContainer");
console.dir(cardContainer);
console.log(cardContainer);

const cardForResume = document.getElementById("productCardRow"); 
console.dir(cardForResume);

const cardStructure = {
    btnAdd: document.getElementById("btnAddItem"),
    btnDelete: document.getElementById("btnDeleteItem"),
    btnReduce: document.getElementById("btnReduceItem"),
    inputAmount: document.getElementById("inputAmount"), 
    inputPrice: document.getElementById("inputPrice")
}

cardStructure.btnAdd.addEventListener("click", () => {
    cardStructure.inputAmount.value++;
    // cardStructure.inputPrice.value = cardStructure.inputAmount.value * cardStructure.inputPrice.value;
    console.log(cardStructure.inputPrice.value);
    console.dir(cardStructure.inputPrice.value);
})


//! Para agregar en la sección de productos
// cardStructure.btnAdd.addEventListener("click", () => {
//     cardContainer.innerHTML = 
//     `
//     <div class="row py-3 mb-3" id="productCardRow">
//                                 <div class="col-4">
//                                     <div class="bg-image cardImg rounded">
//                                         <img class="w-100 rounded" src="../img/products/Argentina/Argentina-1978-primera.svg" alt="producto">
//                                     </div>
//                                 </div>
//                                 <div class="col-5">
//                                     <h6>Selección de Alemania 1954</h6>
//                                     <small>Camiseta titular</small>
//                                     <ul class="list-unstyled my-2">
//                                         <span>$4900</span>
//                                     </ul>
//                                     <ul class="list-unstyled mt-5">
//                                         <button class="mt-1 me-1 mb-1 p-2 material-symbols-sharp" id="btnDeleteItem">
//                                             delete
//                                         </button>
//                                         <button class="mt-1 me-1 mb-1 p-2 material-symbols-sharp" id="btnReduceItem">
//                                             remove
//                                         </button>
//                                         <button class="mt-1 me-1 mb-1 p-2 material-symbols-sharp" id="btnAddItem">
//                                             add
//                                         </button>
//                                     </ul>
//                                 </div>
//                                 <div class="col-3 px-4">
//                                     <label for="amountProducts1">Cantidad:</label>
//                                     <input type="text" class="form-control mb-2 mx-1" placeholder="¿Cuántos?" value="1" id="amountProducts1">
//                                     <label for="output1">Valor total:</label>
//                                     <input type="text" class="form-control mt-2 mx-1" id="output1" value="$4900" disabled>
//                                 </div>
//                             </div>
//                             <!--! hr tag -->
//                             <hr>
//     `
// })


// Cambios dinámicos en el resumen del carro







// Gestión dinámica de elementos que se agregan en el carro y en el resumen del carro
