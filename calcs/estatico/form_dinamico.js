(function ($) {
    explicacion = function () {
        $("#id_chosen_method").change(function () {
            var eleccion = $("#id_chosen_method").val();
            // Add or remove fields depending of mothed chosen
            if (eleccion !== "horas_frio" && eleccion !== "dias_grado") {
                $("#id_base_temp").hide("slow");
                $("#id_sup_temp").hide("slow");
                $("label[for|='id_base_temp']").hide("slow");
                $("label[for|='id_sup_temp']").hide("slow");
            }
            else {
                $("#id_base_temp").show("slow");
                $("#id_sup_temp").show("slow");
                $("label[for|='id_base_temp']").show("slow");
                $("label[for|='id_sup_temp']").show("slow");
            }
            // Search for the explanation of chosen method
            $.get("/calcs/explanation/" + eleccion + "/", function (data) {
                if (data)
                {
                    $("#explanation_text").html(data);
                }
                else
                {
                    $("#explanation_text").html("sin explicación")
                }
            });
        });
    };
})(jQuery);
