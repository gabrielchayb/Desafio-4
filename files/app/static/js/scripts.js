var currentPage = window.location.pathname;
var pageName = currentPage.split("/").pop();

var body = document.getElementById('body');

if (pageName == 'home') {
    body.style.backgroundImage  = "url('../static/img/fundo.png')";
} else {
    body.style.backgroundImage  = "url('../static/img/fundo2.png')";
};