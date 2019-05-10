//Author: Matt, Lukas
//Purpose: To handle the validation of the login page
//Parameters: None
//Return Value: None

var attempt = 3 //start with 3 attempts at login before lockout

$(document).ready(function() {
	$("#loginform").on("submit", function() {

		var username = document.getElementById("exampleInputUser").value;
		var password = document.getElementById("exampleInputPassword1").value;
		if ( username == "admin" && password == "admin"){
			alert ("Login successfully");
			window.location.href = "adminpage.html";
		}
		else{
			attempt = attempt-1; //decrement the number of attempts left
			alert("Incorrect credentials. You have "+attempt+" attempts left;");

			// Disable login after 3 unsuccessfuly attempts
			if (attempt == 0){
				//Disable login elements
				$("#sumbit_btn").attr("disabled", true);
			}
		}
	})
});
