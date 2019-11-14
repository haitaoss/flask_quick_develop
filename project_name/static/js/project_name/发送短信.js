$(function () {
    $("#form1").submit(function (e) {
        // 阻止提交行为
        e.preventDefault();
        // 向后端发送请求
        var mobile = $("#mobile").val();

        $.get("/api/v1.0/user/sms_codes/" + mobile,
            function (resp) {
                alert(resp.errmsg);
            }, 'json');

    });


});