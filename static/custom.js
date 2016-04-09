/**
 * Created by sniper on 25/02/16.
 */
$(document).ready(function(){
    $("a#about").click(function(e){
        e.preventDefault();
        $("div#modal_about").modal('setting', 'closable', false).modal('show');
    });
});
