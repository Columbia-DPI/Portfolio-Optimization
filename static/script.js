$("span, .overlay").click(function () {
    $('body').css({'overflow':'visible'});
    $(".show").fadeOut();
});

function clickCalculate(elmnt) {
    var datum = {
        "weights": [{
            "w1": ".1"
        }, {
            "w2": ".1"
        }, {
            "w3": ".8"
        }],
        "tickers": [{
            "t1": "AAA"
        }, {
            "t2": "AAA"
        }, {
            "t3": "AAA"
        }]
    };
    var datum = {
        "weights": [$("input[name='w1']").val(),
            $("input[name='w2']").val(),
            $("input[name='w3']").val()
        ],
        "tickers": [$("input[name='t1']").val(),
            $("input[name='t2']").val(),
            $("input[name='t3']").val()
        ]
    };
    $.ajax({
        type: 'POST',
        url: '/plot',
        data: JSON.stringify({
            Datum: datum
        }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data) {
            var $src = $(this).attr("src");
            $(".show").fadeIn();
            $('body').css({'overflow':'hidden'});
            $(".img-show img").attr("src", "data:image/png;base64," + data['b64encoded']);
        },
        failure: function(errMsg) {
            alert(errMsg);
        }
    });
}

function scrollToHowto() {
    const y = document.getElementById("howdoes").getBoundingClientRect().top + window.scrollY;
    window.scroll({
      top: y,
      behavior: 'smooth'
    });
}

function scrollToSimulator() {
    const y = document.getElementById("simulator").getBoundingClientRect().top + window.scrollY;
    window.scroll({
      top: y,
      behavior: 'smooth'
    });
}