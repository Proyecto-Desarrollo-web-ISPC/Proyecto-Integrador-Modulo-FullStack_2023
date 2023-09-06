// import {}



// Estructura de la tarjeta para el resumen del carro
const cardContainer = document.getElementById("cardContainer");
// console.dir(cardContainer);

const cardForResume = document.getElementById("productCardRow"); 
// console.dir(cardForResume);

const listStructure = {
    btnAdd: document.getElementById("btnAddItem"),
    btnDelete: document.getElementById("btnDeleteItem"),
    btnReduce: document.getElementById("btnReduceItem"),
    inputAmount: document.getElementById("inputAmount"), 
    inputPrice: document.getElementById("inputPrice")
}

listStructure.btnAdd.addEventListener("click", () => {
    let productsAmount = listStructure.inputAmount.value++;
    let totalPrice = listStructure.inputPrice.value;
    if (productsAmount++){
        
    }
    // console.log(totalPrice);

})


//! Para agregar en la sección de productos
// listStructure.btnAdd.addEventListener("click", () => {
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

