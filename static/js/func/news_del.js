;
var news_del_ops = {
        init: function () {
            this.eventBind()
        },
        eventBind: function () {
            $(".news_info_del_wrap .do_news_info_del").click(function () {
                var btn_target = $(this);
                if (btn_target.hasClass("disabled")) {
                    common_ops.alert("正在处理！！！请不要重复点击！");
                    return;
                }
                var news_id = $(".do_news_info_del").attr("id")
                btn_target.addClass("disabled");
                $.ajax({
                url: common_ops.buildUrl("/logged/news_info"),
                type: "POST",
                data: {
                    news_id: news_id,
                },
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/logged/news");
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
    news_del_ops.init()
});