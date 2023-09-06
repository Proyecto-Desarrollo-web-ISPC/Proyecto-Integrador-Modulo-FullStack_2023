let productosAgregados = [];

const cardStructure = {
    addToCardBtn: document.getElementsByClassName("addProductBtn"),
}

class Product {
    constructor(pais, tipo){
        this._pais = pais;
        this._tipo = tipo;
    }
    get pais(){
        return this._pais;
    }
    get tipo(){
        return this._tipo;
    }
}



