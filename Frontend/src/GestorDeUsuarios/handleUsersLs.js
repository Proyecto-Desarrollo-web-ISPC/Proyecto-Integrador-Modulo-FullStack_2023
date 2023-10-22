export function saveUserLocalStorage(newUser){
    let newUsers;
    newUsers = getUsersLocalStoraged();
    newUsers.push(newUser);
    localStorage.setItem('users', JSON.stringify(newUsers));
};

export function getUsersLocalStoraged(){
    let usersLocalStoraged;
    if(localStorage.getItem('users') === null){
        usersLocalStoraged = [];
    } else {
        usersLocalStoraged = JSON.parse(localStorage.getItem('users'));
    };
    return usersLocalStoraged;
};