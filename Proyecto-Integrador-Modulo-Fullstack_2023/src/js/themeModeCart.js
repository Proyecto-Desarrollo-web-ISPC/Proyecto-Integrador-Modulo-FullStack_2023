// Creación de selector de elementos de navegación y estéticos de la estructura del carro
const basicStructure = {
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
    footerItem: document.getElementsByClassName("footerItem"),
    card: document.getElementsByClassName("card"),
    // modalContainer: document.querySelector(".modalContainer"), //! Buscarle la forma de poder manipular el modal tanto acá como en las otras páginas
    // modalTitle: document.querySelector(".modalTitle")
}

// Creación de objeto para manejo del modo Dark y Light
const toggleMode = {
    lightMode: function(){
        basicStructure.togglerBtnLM.setAttribute("class", "mx-2 navItem d-none");
        basicStructure.togglerBtnDM.setAttribute("class", "mx-2 navItem d-block");
        const colorBodyLightMode = "linear-gradient(120deg, #f5f5f5 10%, #366608 80%)";
        basicStructure.body.style.background = colorBodyLightMode;
        basicStructure.navbar.setAttribute("data-bs-theme", "light");
        basicStructure.footer.style.background = "#f5f5f5";
        basicStructure.mainTitle.style.color = "#222222";
        // basicStructure.logo.src = "imgPath";
        for(let i = 0; i < basicStructure.h2.length; i++){
            basicStructure.h2[i].style.color = "#222222";
        };
        for(let i = 0; i < basicStructure.h3.length; i++){
            basicStructure.h3[i].style.color = "#222222";
        };
        for(let i = 0; i < basicStructure.h4.length; i++){
            basicStructure.h4[i].style.color = "#222222";
        };
        for(let i = 0; i < basicStructure.h5.length; i++){
            basicStructure.h5[i].style.color = "#222222";
        }
        for(let i = 0; i < basicStructure.h6.length; i++){
            basicStructure.h6[i].style.color = "#222222";
        }
        for(let i = 0; i < basicStructure.p.length; i++){
            basicStructure.p[i].style.color = "#222222";
        }
        for(let i = 0; i < basicStructure.a.length; i++){
            basicStructure.a[i].style.color = "#222222";
        }
        for(let i = 0; i < basicStructure.label.length; i++){
            basicStructure.label[i].style.color = "#222222";
        }
        for(let i = 0; i < basicStructure.card.length; i++){
            basicStructure.card[i].setAttribute("data-bs-theme", "light");
        }
        for(let i = 0; i < basicStructure.footerItem.length; i++){
            basicStructure.footerItem[i].style.color = "#222222";
        }
        // for(let i = 0; i < basicStructure.modalContainer.length; i++){
        //     basicStructure.modalContainer[i].setAttribute("data-bs-theme", "light"); //! Buscarle la forma de poder manipular el modal tanto acá como en las otras páginas
        // }
        // for(let i = 0; i < basicStructure.modalTitle.length; i++){
        //     basicStructure.modalTitle[i].style.color = "#222222";
        // }
    },
    darkMode: function(){
        basicStructure.togglerBtnDM.setAttribute("class", "mx-2 navItem d-none");
        basicStructure.togglerBtnLM.setAttribute("class", "mx-2 navItem d-block");
        const colorBodyDarkMode = "linear-gradient(120deg, #222222 10%, #366608 80%)";
        basicStructure.body.style.background = colorBodyDarkMode;
        basicStructure.navbar.setAttribute("data-bs-theme", "dark");
        basicStructure.footer.style.background = "#222222";
        basicStructure.mainTitle.style.color = "#f5f5f5";
        // basicStructure.logo.src = "imgPath"               //Agregar path a nuevo logo
        for(let i = 0; i < basicStructure.h2.length; i++){
            basicStructure.h2[i].style.color = "#f5f5f5";
        };
        for(let i = 0; i < basicStructure.h3.length; i++){
            basicStructure.h3[i].style.color = "#f5f5f5";
        };
        for(let i = 0; i < basicStructure.h4.length; i++){
            basicStructure.h4[i].style.color = "#f5f5f5";
        };
        for(let i = 0; i < basicStructure.h5.length; i++){
            basicStructure.h5[i].style.color = "#f5f5f5";
        }
        for(let i = 0; i < basicStructure.h6.length; i++){
            basicStructure.h6[i].style.color = "#f5f5f5";
        }
        for(let i = 0; i < basicStructure.p.length; i++){
            basicStructure.p[i].style.color = "#f5f5f5";
        }
        for(let i = 0; i < basicStructure.a.length; i++){
            basicStructure.a[i].style.color = "#f5f5f5";
        }
        for(let i = 0; i < basicStructure.label.length; i++){
            basicStructure.label[i].style.color = "#f5f5f5";
        }
        for(let i = 0; i < basicStructure.p.length; i++){
            basicStructure.p[i].style.color = "#f5f5f5"
        }
        for(let i = 0; i < basicStructure.card.length; i++){
            basicStructure.card[i].setAttribute("data-bs-theme", "dark");
        }
        for(let i = 0; i < basicStructure.footerItem.length; i++){
            basicStructure.footerItem[i].style.color = "#f5f5f5";
        }
        // for(let i = 0; i < basicStructure.modalContainer.length; i++){
        //     basicStructure.modalContainer[i].setAttribute("data-bs-theme", "light"); //! Buscarle la forma de poder manipular el modal tanto acá como en las otras páginas
        // }
        // for(let i = 0; i < basicStructure.modalTitle.length; i++){
        //     basicStructure.modalTitle[i].style.color = "#222222";
        // }
    }
}

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

console.dir(basicStructure.togglerBtnDM);

export {basicStructure, setDarkMode, setLightMode};