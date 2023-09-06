import {productosAgregados} from "./dynamicProducts"

let productos = []

for(let i = 0; i < productosAgregados.length; i++){
    productos.push(productosAgregados);
}

function calcularSubtotal(productos){
    let subtotal = 0;

    for (let i = 0; i < productos.length; i++) {
        subtotal += productos[i];
    }
    return subtotal;
}

const subtotal = calcularSubtotal(productos);

mostrarSubtotal()
function mostrarSubtotal(){
    const outputSubtotal = document.getElementById("outputSubtotal");
    outputSubtotal.innerHTML(`El total de sus productos es ${subtotal}`);
}