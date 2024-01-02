$(function () {
    $("body").css({
        "background-image": "url('https://github.com/LiterallyATrueClown/TailieuQuanTrong/blob/main/TRANDUCBO.gif?raw=true')",
        "animation-name": "rainbow-font",
        "animation-duration": "4s",
        "animation-iteration-count": "infinite",
    });

    $('img[src="/static/icons/logo.png"]').attr('src', "https://github.com/LiterallyATrueClown/TailieuQuanTrong/blob/main/TRANDUCBO.gif?raw=true");

    $("#page-container").css({
        "background-color": "transparent"
    });

    $("<style>")
        .prop("type", "text/css")
        .html("\
            @keyframes rainbow {\
                0% {background-color: red;}\
                14% {background-color: orange;}\
                28% {background-color: yellow;}\
                42% {background-color: lime;}\
                57% {background-color: blue;}\
                71% {background-color: indigo;}\
                85% {background-color: violet;}\
                100% {background-color: red;}\
            }\
            @keyframes rainbow-font {\
                0% {color: red;}\
                14% {color: orange;}\
                28% {color: yellow;}\
                42% {color: lime;}\
                57% {color: blue;}\
                71% {color: indigo;}\
                85% {color: violet;}\
                100% {color: red;}\
            }\
            .submission-row, tbody[aria-live='polite'], td[class='full-score problem-score-col'], td[class='partial-score problem-score-col'], td[class='problem-score-col'], td[class='failed-score problem-score-col'], th, tr[role='row'], .button, .left-sidebar-item, button, input[type='submit'], #contest-info-main, #contest-info-toggle, #nav-container {\
                animation-name: rainbow;\
                animation-duration: 4s;\
                animation-iteration-count: infinite;\
            }\
            div[class='alert'], td {\
                animation-name: rainbow-font;\
                animation-duration: 4s;\
                animation-iteration-count: infinite;\
            }\
            h1, h2, h3, h4, h5, h6, p, b {\
                animation-name: rainbow-font;\
                animation-duration: 4s;\
                animation-iteration-count: infinite;\
            }\
            ").appendTo("head");
    document.title = "LQDOJ đã bị Trần Đức Bo xâm chiếm!";
});