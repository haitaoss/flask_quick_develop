$(function () {
    $("#form1").submit(function (e) {
        // 阻止浏览器的表单提交行为
        e.preventDefault();

        // 获取表单数据
        var data = {};

        $("#form1").serializeArray().map(function (x) {
            data[x.name] = x.value;
        });

        //发起ajax post 请求,数据是json数据
        $.ajax({
                url: "/api/v1.0/order/pay",
                type: "post",
                data: JSON.stringify(data),
                dataType: "json",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFTOKEN": getCookie("csrf_token")

                },
                success: function (resp) {
                    if (resp.errno == "0") {
                        window.open(resp.data.pay_url);
                        // 支付成功
                        return;
                    }
                    alert(resp.errmsg);
                }
            }
        )
    });

    $("#btn1").click(function () {
        $.get("/api/v1.0/order/check", function (resp) {
            if (resp.errno == "0") {
                // 进行对应的操作
                alert(resp.errmsg);
                return;
            }
            alert(resp.errmsg);
        });
    });
});
