;

var func_news_add_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".add_wrap .do-add").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在处理！！！请不要重复点击！");
                return;
            }
            var news_title = $(".add_wrap input[name = news_title]").val();
            var news_img = $(".add_wrap input[name = news_img]").val();
            var news_src = $(".add_wrap input[name = news_src]").val();
            var news_desc = $(".add_wrap input[name = news_desc]").val();

            if (news_title == undefined || news_title.length < 1) {

                common_ops.alert("请输入资讯标题");
                return;
            }
            if (news_img == undefined || news_img.length < 1) {
                common_ops.alert('请输入资讯封面图网址');
                return;
            }
            if (news_src == undefined || news_src.length < 1) {
                common_ops.alert("请输入资讯文章网址！");
                return;
            }
            if (news_desc == undefined || news_desc.length < 1) {
                common_ops.alert("请输入资讯文章简介！");
                return;
            }
            btn_target.addClass("disabled");
            $.ajax({
                url: common_ops.buildUrl("/logged/news_add"),
                type: "POST",
                data: {
                    news_img: news_img,
                    news_title: news_title,
                    news_src: news_src,
                    news_desc: news_desc,
                },
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/logged/news_add");
                        };
                    }
                    common_ops.alert(res.msg, callback);
                }
            })
        })
    }
};

$(document).ready(function () {
    func_news_add_ops.init();
});