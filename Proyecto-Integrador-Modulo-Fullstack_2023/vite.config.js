import {resolve} from 'node:path'

export default {
    server: {
        port: "5555",
    },
    css:{
        devSourcemap: true,
    },
    build: {
        emptyOutDir: true,
        rollupOptions:{
            input:{
                about: resolve('./pages/about.html'),
                cart: resolve('./pages/cart.html'),
                contact: resolve('./pages/contact.html'),
                products: resolve('./pages/products.html'),
                index: resolve('./index.html')
            }
        }
    }
}

// Usá 'npm run build' una vez que se haya finalizado el proyecto
// Se va a crear una carpeta llamada dist que es la que se debe subir como versión final 
