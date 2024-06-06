$(document).ready(function(){
    $('#tblEditavel tbody tr td').dblclick(function(){
        if ($('td > input').length > 0){
            return;
        }
        var conteudoOriginal = $(this).text();
        var novoElemento = $('<input/>', {type:'text', value:conteudoOriginal});
        $(this).html(novoElemento.bind('blur keydown', function(e){
            var keyCode = e.which;
            if( keyCode == 13 ){
                var conteudoNovo = $(this).val();
                if ( conteudoNovo != ""){
                    $(this).parent().html(conteudoNovo);
                }
            else {
                alert("é Necessario inserir um valor")
            }}
                if (e.type == "blur"){
                    $(this).parent().html(conteudoOriginal);
                }}));
                $(this).children().select();
            })})