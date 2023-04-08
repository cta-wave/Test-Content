$(document).ready(function() {
    //localStorage.removeItem('eulaAccepted'); //toggle for debug
    if (localStorage.getItem('eulaAccepted') != 'yes') {
        const eulaModel = document.getElementById('eulaDialog');
        eulaModel.showModal();
    }
});

const acceptEulaButton = document.getElementById("acceptEula");
acceptEulaButton.addEventListener("click", () => {
    localStorage.setItem('eulaAccepted', 'yes');
});
