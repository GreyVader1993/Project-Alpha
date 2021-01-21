let xhr = new XMLHttpRequest();
xhr.open('get', 'https://api.github.com/networks/GreyVader1993/Project-Alpha/events');
xhr.send();

xhr.onload = function() {
    console.log(xhr.response);
};