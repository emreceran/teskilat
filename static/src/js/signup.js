odoo.define('teskilat.signup', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    $(document).ready(function () {
        $('#il_id').change(function () {
            var il_id = parseInt($(this).val(), 10);

            ajax.jsonRpc('/get_districts', 'call', {'il_id': il_id}).then(function (data) {
                if (data.error) {
                    console.error("Hata:", data.error);
                    return;
                }
                var $ilce = $('#ilce_id');
                $ilce.empty();
                $ilce.append('<option value="">Select İlçe</option>');
                $.each(data, function (index, ilce) {
                    $ilce.append('<option value="' + ilce.id + '">' + ilce.name + '</option>');
                });
            }).catch(function (error) {
                console.error("İlçeleri yüklerken hata oluştu:", error);
            });
        });

        $('#ilce_id').change(function () {
            var ilce_id = parseInt($(this).val(), 10);

            ajax.jsonRpc('/get_schools', 'call', {'ilce_id': ilce_id}).then(function (data) {
                if (data.error) {
                    console.error("Hata:", data.error);
                    return;
                }
                var $lise = $('#lise_id');
                $lise.empty();
                $lise.append('<option value="">Select Lise</option>');
                $.each(data, function (index, lise) {
                    $lise.append('<option value="' + lise.id + '">' + lise.name + '</option>');
                });
            }).catch(function (error) {
                console.error("Liseleri yüklerken hata oluştu:", error);
            });
        });
    });
});
