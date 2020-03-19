;

var goods_add_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".goods_add_wrap .do-goods_add").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在处理！！！请不要重复点击！");
                return;
            }
            var title = $(".goods_add_wrap input[name = title]").val();
            var brand = $(".goods_add_wrap input[name = brand]").val();
            var arctic = $(".goods_add_wrap input[name = arctic]").val();
            var regist_date = $(".goods_add_wrap input[name = regist_date]").val();
            var mileage = $(".goods_add_wrap input[name = mileage]").val();
            var emissions = $(".goods_add_wrap input[name = emissions]").val();
            var gear = $(".goods_add_wrap input[name = gear]").val();
            var price = $(".goods_add_wrap input[name = price]").val();
            var describe = $(".goods_add_wrap input[name = describe]").val();
            var picture1 = $(".goods_add_wrap input[name = picture1]").val();
            var picture2 = $(".goods_add_wrap input[name = picture2]").val();
            var picture3 = $(".goods_add_wrap input[name = picture3]").val();
            var picture4 = $(".goods_add_wrap input[name = picture4]").val();
            var picture5 = $(".goods_add_wrap input[name = picture5]").val();
            var picture6 = $(".goods_add_wrap input[name = picture6]").val();
            var cars_local = $(".goods_add_wrap input[name = cars_local]").val();
            var img_desc = $(".goods_add_wrap input[name = img_desc]").val();

            if (title == undefined || title.length < 1) {

                common_ops.alert("请输入商品标题");
                return;
            }
            if (img_desc == undefined || img_desc.length < 1) {

                common_ops.alert("请输入图文详情链接");
                return;
            }
            if (brand == undefined || brand.length < 1) {
                common_ops.alert('请输入车辆品牌');
                return;
            }
            if (arctic == undefined || arctic.length < 1) {
                common_ops.alert("请输入车辆型号！");
                return;
            }
            if (regist_date == undefined || regist_date.length < 1) {
                common_ops.alert("请输入上牌年月！");
                return;
            }
            if (mileage == undefined || mileage.length < 1) {
                common_ops.alert("请输入表显里程！");
                return;
            }
            if (emissions == undefined || emissions.length < 1) {
                common_ops.alert("请输入排放标准！");
                return;
            }
            if (gear == undefined || gear.length < 1) {
                common_ops.alert("请输入挡位类型！");
                return;
            }
            if (price == undefined || price.length < 1) {
                common_ops.alert("请输入价格！");
                return;
            }
            if (cars_local == undefined || cars_local.length < 1) {
                common_ops.alert("请输入车牌归属地！");
                return;
            }
            if (describe == undefined || describe.length < 1) {
                common_ops.alert("请输入车况描述！");
                return;
            }
            if (picture1 == undefined || picture1.length < 1) {
                common_ops.alert("请至少添加一张照片地址！");
                return;
            }
            btn_target.addClass("disabled");
            $.ajax({
                url: common_ops.buildUrl("/logged/goods_add"),
                type: "POST",
                data: {
                    title: title,
                    brand: brand,
                    arctic: arctic,
                    regist_date: regist_date,
                    mileage: mileage,
                    emissions: emissions,
                    gear: gear,
                    price: price,
                    img_desc: img_desc,
                    cars_local: cars_local,
                    describe: describe,
                    picture1: picture1,
                    picture2: picture2,
                    picture3: picture3,
                    picture4: picture4,
                    picture5: picture5,
                    picture6: picture6,
                },
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/logged/goods_add");
                        };
                    }
                    common_ops.alert(res.msg, callback);
                }
            })
        })
    }
};

$(document).ready(function () {
    goods_add_ops.init();
});
