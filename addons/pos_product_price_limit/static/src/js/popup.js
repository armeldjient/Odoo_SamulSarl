/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
/* License URL : <https://store.webkul.com/license.html/> */
odoo.define('pos_product_price_limit.popups', function (require) {
    "use strict";
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { onMounted } = owl;

    class MinMxQtyPopupWidget extends AbstractAwaitablePopup {
        setup() {
            super.setup();
            onMounted(this.onMounted);
        }
        onMounted() {
            // to focus on input button when popup opens
            $('#wk_price_val').focus();
            // to proceed when 'enter' key is pressed 
            $("#wk_price_val").keyup(function (event) {
                if (event.keyCode === 13) {
                    $(".wk_proceed").click();
                }
            });
        }
        click_wk_cancel() {
            this.cancel();
        }
        click_proceed(e) {
            // shows appropriate restriction when a min/max condition is not met 
            // else proceeds to change price of the selected product.
            var self = this;
            var product = self.props.sel_line.product;
            var new_price = $('#wk_price_val').val();
            if (product && new_price) {
                if (!product.enable_min_price) {
                    if (product.enable_max_price && new_price <= product.max_price && new_price > product.lst_price) {
                        self.props.sel_line.set_unit_price(new_price);
                        self.props.sel_line.price_manually_set = true;
                        self.cancel();
                    } else {
                        if (new_price < product.lst_price) {
                            $('.lst_price_error_max').show();
                            setTimeout(() => {
                                $('.lst_price_error_max').hide();
                            }, 3000);
                        } else {
                            $('.max_error').show();
                            setTimeout(() => {
                                $('.max_error').hide();
                            }, 3000);
                        }
                    }
                } else if (!product.enable_max_price) {
                    if (product.enable_min_price && new_price >= product.min_price && new_price < product.lst_price) {
                        self.props.sel_line.set_unit_price(new_price);
                        self.props.sel_line.price_manually_set = true;
                        self.cancel();
                    } else {
                        if (new_price > product.lst_price) {
                            $('.lst_price_error_min').show();
                            setTimeout(() => {
                                $('.lst_price_error_min').hide();
                            }, 3000);
                        } else {
                            $('.min_error').show();
                            setTimeout(() => {
                                $('.min_error').hide();
                            }, 3000);
                        }
                    }
                } else {
                    if (new_price >= product.min_price && new_price <= product.max_price) {
                        self.props.sel_line.set_unit_price(new_price);
                        self.props.sel_line.price_manually_set = true;
                        self.cancel();
                    } else {
                        if (new_price < product.min_price) {
                            $('.min_error').show();
                            setTimeout(() => {
                                $('.min_error').hide();
                            }, 3000);
                        }
                        if (new_price > product.max_price) {
                            $('.max_error').show();
                            setTimeout(() => {
                                $('.max_error').hide();
                            }, 3000);
                        }
                    }
                }
            }
        }
    }
    MinMxQtyPopupWidget.template = 'MinMxQtyPopupWidget';
    Registries.Component.add(MinMxQtyPopupWidget);
});