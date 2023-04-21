$(document).ready(function () {
    $.ajax({
        url: "/api/test"
    }).then(function (data) {
        $('.quote-symbol').append(data.symbol);
        $('.quote-price').append(data.price);
    });
});