import { saveUserLocalStorage } from "./handleUsersLs.js";

export function buildUser(userInfo){ //* Getting register formData
    class User {
        constructor(name, lastName, dni, address, email, password, id){
            this.name = name;
            this.lastName = lastName;
            this.dni = dni;
            this.address = address;
            this.email = email;
            this.password = password;
            this.id = id;
        };
    };
    let newUser = new User(userInfo.name, userInfo.lastName, userInfo.dni, userInfo.address, userInfo.email, userInfo.password, userInfo.id);
    saveUserLocalStorage(newUser);
};