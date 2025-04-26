odoo.define('cr_pos_payment_method_icon.PaymentScreen', function(require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    var core = require('web.core');
    var _t = core._t;

    const PaymentScreenIcon = PaymentScreen => class extends PaymentScreen {
        getImageUrl(method) {
            var url = '';
            if (method.id) {
                url = `/web/image?model=pos.payment.method&id=${method.id}&field=payment_icon_image`;
            }
            return url;
        }
    };

    Registries.Component.extend(PaymentScreen, PaymentScreenIcon);

    return PaymentScreen;
});
