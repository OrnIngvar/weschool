/* Author: Örn Ingvar & Davíð Halldór

 */

var progval = 0;

function validateForm() {
    var div_count = 0;
    var radio_count = 0;
    $('.question_div').each(function () {
        div_count += 1;
        $( $(this).find('input:radio') ).each(function() {
            if( $(this).is(':checked') ) {
                radio_count += 1;
            }
        });
    })
    if( div_count === radio_count){
        return true;
    }else{
        return false;
    }
}

function updateProgress( maxVal ) {
    progval += 1;
    $( '#progress' ).html('Exam progress: <progress value='+progval+' max='+maxVal+'></progress>');
}




