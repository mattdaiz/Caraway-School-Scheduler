// JavaScript source code
$( document ).ready(function() {
    $('.button').each(function(){
       $(this).click(function(){
        var username_input =  $(this).closest('tr').find(".username_input").text();
        var firstname_input =  $(this).closest('tr').find(".first_input").text();
        var lastname_input =  $(this).closest('tr').find(".last_input").text();
        $("#user_fill").val(username_input);
        $("#first_fill").val(firstname_input);
        $("#last_fill").val(lastname_input);
    });
   });
});