export function checkLoginStatus(isUserLoggedIn) {
    const logBtnsContainer = document.getElementById('log');
    const loginBtn = logBtnsContainer.querySelector('#loginBtn');
    const logoutBtn = logBtnsContainer.querySelector('#logoutBtn');

    isUserLoggedIn.connectSession = JSON.parse(localStorage.getItem('isUserLoggedIn'));

    if (Boolean(isUserLoggedIn.connectSession) === true) {
        loginBtn.classList.add('d-none');
        logoutBtn.classList.remove('d-none');

    } else {
        loginBtn.classList.remove('d-none');
        logoutBtn.classList.add('d-none');
    };
};

export function logOutUser(isUserLoggedIn){ //* Getting isUserLoggedIn object
    let userSessionStatus = isUserLoggedIn;
    if(Boolean(userSessionStatus) === true){
        isUserLoggedIn = false;
        localStorage.setItem("isUserLoggedIn", JSON.stringify(isUserLoggedIn));
        alert('¡Hasta la próxima!')
        setTimeout(() => {
            window.location.reload();
        }, 3000);
    };
};