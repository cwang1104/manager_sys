;
var goods_del_ops = {
        init: function () {
            this.eventBind()
        },
        eventBind: function () {
            $(".goods_del_wrap .do_goods_del").click(function () {
                var btn_target = $(this);
                if (btn_target.hasClass("disabled")) {
                    common_ops.alert("正在处理！！！请不要重复点击！");
                    return;
                }
                var goods_id = $(".do_goods_del").attr("id");
                btn_target.addClass("disabled");

                $.ajax({
                url: common_ops.buildUrl("/logged/goods_info"),
                type: "POST",
                data: {
                    goods_id: goods_id,
                },
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/logged/goods");
                        };
                    }
                    common_ops.alert(res.msg, callback);
                }
            })


            })
        }
    }
;

$(document).ready(function () {
    goods_del_ops.init()
});