// JavaScript source code
function logout() {
    window.location.href = "login.html";
}

$(document).ready(function () {
    $(".nav a").on("click", function () {

        var newactive = $.trim($(this).text());
        console.log(newactive);

        $(".nav a").removeClass("active");
        $(this).addClass("active");

        $(".h2").text(newactive);

        if (newactive == "Dashboard") {
            $("#div_content").text("Welcome");
        }

        else if (newactive == "Edit Accounts") {
            $("#div_content").load("editaccount.html");
        }

        else if (newactive == "Schedule") {
            $("#div_content").load("test.html");
        }

        else if (newactive == "Account Info") {
            $("#div_content").text("Account info page");
        }

        else if (newactive == "Create Account") {
            $("#div_content").load("createaccount.html");
        }

        else if (newactive == "Statistics") {
            $("#div_content").load("statistics.html");
        }


    })
});