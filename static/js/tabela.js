$(document).ready(function(){
    $('#tblEditavelCable tbody tr td, #tblEditavelGBIC tbody tr td').dblclick(function(){
        if ($('td > input').length > 0){
            return;
        }

        var conteudoOriginal = $(this).text();
        var coluna = $(this).attr('id');
        var linha = $(this).closest('tr').data('id');
        var tabela = $(this).closest('table').attr('id').replace('tblEditavel', ''); 

        var novoElemento = $('<input/>', {
            type: 'text',
            value: conteudoOriginal
        });

        $(this).html(novoElemento);
        novoElemento.focus().select();

        novoElemento.bind('blur keydown', function(e){
            var keyCode = e.which;

            if (keyCode == 13 || e.type == 'blur') {
                var conteudoNovo = $(this).val();

                if (conteudoNovo !== "") {
                    $(this).parent().html(conteudoNovo);

                    if (conteudoNovo !== conteudoOriginal) {
                        console.log({
                            id: linha,
                            table: tabela,
                            column: coluna,
                            value: conteudoNovo
                        });

                        $.ajax({
                            url: '/update',
                            method: 'POST',
                            data: {
                                id: linha,
                                table: tabela,
                                column: coluna,
                                value: conteudoNovo
                            },
                            success: function(response) {
                                alert(response.message);
                            },
                            error: function(xhr, status, error) {
                                alert('Failed to update the value. Error: ' + xhr.responseText);
                                $(this).parent().html(conteudoOriginal);
                            }
                        });
                    }
                } else {
                    alert("É necessário inserir um valor");
                    $(this).parent().html(conteudoOriginal);
                }
            }
        });
    });
});
