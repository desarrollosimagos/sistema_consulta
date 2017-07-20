// Funcion 
$(document).ready(function() { // Apertura del ready
	$('#username').focus()
	$( "#menu" ).menu();
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de opción en el combo de estado
////////////////////////////////////////////////////////////////////////////////////////////////////////
$('#id_cod_estado').change(function() {
	var id_est = $('#id_cod_estado').val();
	
	$('#id_cod_municipio').find('option:gt(0)').remove().end();
	if (id_est > 0) {
	    $.get('/parroquia/busqueda_ajax/', {'id':id_est}, function(data) {
		var option = "";
		$.each(data, function(i) {
		    option += "<option value=" + data[i].fields.cod_municipio + ">" + data[i].fields.municipio + "</option>";
		});
		$('#id_cod_municipio').append(option);
	    }, 'json');
	}
	listar_centros()	
});

////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de option se obtiene el pk de municipio
////////////////////////////////////////////////////////////////////////////////////////////////////////
$('#id_cod_municipio').change(function() {
	var id_est  = $('#id_cod_estado').val();
	var id_mun = $('#id_cod_municipio').val();
	if (id_est > 0 && id_mun > 0) {
	    $.get('/centro_votacion/busquedaajax/', {'id_est':id_est,'id_mun':id_mun}, function(data) {
		    	$('#id_mun').val(data)
	    }, 'json');
	}
	listar_centros()	
});

////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de option en el combo municipio
////////////////////////////////////////////////////////////////////////////////////////////////////////
$('#id_cod_municipio').change(function() {
	var id_est  = $('#id_cod_estado').val();
	var id_mun  = $("#id_cod_municipio").val();
	var id_parr = $('#id_cod_parroquia').val();
	
	$('#id_cod_parroquia').find('option:gt(0)').remove().end();
	if (id_est > 0 && id_mun > 0) {
		
	    $.get('/parroquia/busqueda_ajax2/', {'id_est':id_est,'id_mun':id_mun}, function(data) {
		var option = "";
		$.each(data, function(i) {
		    option += "<option value=" + data[i].fields.cod_parroquia + ">" + data[i].fields.parroquia + "</option>";
		});
		$('#id_cod_parroquia').append(option);
	
	    }, 'json');
	}
	listar_centros()
	
});
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Al cambiar de option se construye
////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Carga el codigo del centro
////////////////////////////////////////////////////////////////////////////////////////////////////////
$('#id_cod_estado').change(function(){
        var e = $('#id_cod_estado').val();
        $('#id_cod_n').val(e);
        listar_centros()
    });

$('#id_cod_municipio').change(function(){
        var e = $('#id_cod_estado').val();
        var m = $('#id_cod_municipio').val();
        if (m.length == 1){
            a = "0"+m
        }
        else{
            a = m
        }
        $('#id_cod_n').val(e+''+a);
        listar_centros()
    });

    
$('#id_cod_parroquia').change(function(){
        var e = $('#id_cod_estado').val();
        var m = $('#id_cod_municipio').val();
        var p = $('#id_cod_parroquia').val();
        
        if (m.length == 1){
            a = "0"+m
        }
        else{
            a = m
        }
        if (p.length == 1){
            o = "0"+p
        }
        else{
            o = p
        }
        $('#id_cod_n').val(e+''+a+''+o);
        listar_centros()
    });
////////////////////////////////////////////////////////////////////////////////////////////////////////
}); // Cierre del ready
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Funcion global para depurar
////////////////////////////////////////////////////////////////////////////////////////////////////////
function eliminar_data(pk_id, url) {
  id_data= String(pk_id)
  r = confirm("¿Realmente desea eliminar el registro?!");
  if (r == true) {
      location.href=url+id_data;
  }
};
////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////
// Para filtrar los centros de votación al cambiar de option en el combos de estado, municipio y parroquia
////////////////////////////////////////////////////////////////////////////////////////////////////////
function listar_centros() {
	var id_est  = $('#id_cod_estado').val();
	var id_mun  = $("#id_cod_municipio").val();
	var id_parr = $('#id_cod_parroquia').val();
	
	
	$('#id_cod_nuevo').find('option:gt(0)').remove().end();
	if (id_est > 0 && id_mun > 0 && id_parr > 0) {
		
	    $.get('/registro_electoral/busqueda_ajax_centros/', {'id_est':id_est,'id_mun':id_mun,'id_parr':id_parr}, function(data) {
		var option = "";
		$.each(data, function(i) {
		    //alert(String(data[i].pk)+" - "+data[i].fields.c_votacion)
		    option += "<option value=" + String(data[i].fields.cod_n) + ">" + data[i].fields.c_votacion + "</option>";
		});
		$('#id_cod_nuevo').append(option);
	
	    }, 'json');
	}
	
};
