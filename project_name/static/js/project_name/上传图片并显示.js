$(function () {
    $("#form1").submit(function (e) {
        // 阻止默认提交行为
        e.preventDefault();

        //使用插件提交，不需要提取参数，他会帮我们设置好
        $("#form1").ajaxSubmit({
            url: "/api/v1.0/user/avatar",
            type: "post",
            dataType: "json",
            headers: {
                "X-CSRFTOKEN": getCookie("csrf_token")
            },
            success: function (resp) {
                if (resp.errno == "0") {
                    $("#image").attr("src", resp.data.image_url);
                    // 支付成功
                    return;
                }
                alert(resp.errmsg);
            }
        })
    });
});