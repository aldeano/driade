(function($){
    explicacion = function() {
        $("#id_chosen_method").change(function(){
            var eleccion = $("#id_chosen_method").val();
            if (eleccion != "horas_frio")
            {
                $("#id_base_temp").hide("slow");
                $("#id_sup_temp").hide("slow");
                $("label[for|='id_base_temp']").hide("slow");
                $("label[for|='id_sup_temp']").hide("slow");
            }
            else
            {
                $("#id_base_temp").show("slow");
                $("#id_sup_temp").show("slow");
                $("label[for|='id_base_temp']").show("slow");
                $("label[for|='id_sup_temp']").show("slow");
            }
        });
    };
})(jQuery);
