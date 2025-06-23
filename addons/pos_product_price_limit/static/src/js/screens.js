/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
/* License URL : <https://store.webkul.com/license.html/> */
odoo.define('pos_product_price_limit.screens', function (require) {
    "use strict";
    const Registries = require('point_of_sale.Registries');
    const NumpadWidget = require('point_of_sale.NumpadWidget');

    const MinMaxNumpadWidget = (NumpadWidget) =>
        class extends NumpadWidget {
            changeMode(mode) {
                // inherit function to show min/max popup - MinMxQtyPopupWidget when price button is click when 
                // its required conditions are fulfilled
                var self = this;
                var pos = self.env.pos;
                var sel_line = pos.get_order().get_selected_orderline();
                if (sel_line && pos.config.is_restrict_min_max_price && mode == "price") {
                    if ((sel_line.product.enable_min_price && sel_line.product.min_price > 0.00) || (sel_line.product.enable_max_price && sel_line.product.max_price > 0.00)) {
                        self.showPopup('MinMxQtyPopupWidget', {
                            title: this.env._t('Min/Max Price'),
                            body: this.env._t("Enter a price for the Product"),
                            sel_line: sel_line,
                            product: sel_line.product,
                        });
                    } else {
                        super.changeMode(mode)
                    }
                } else {
                    super.changeMode(mode)
                }
            }
        }
    Registries.Component.extend(NumpadWidget, MinMaxNumpadWidget);
});