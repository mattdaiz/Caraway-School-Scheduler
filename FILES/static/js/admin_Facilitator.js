// JavaScript source code
$( document ).ready(function() {
	$("#accountInfo").on("show.bs.modal", function (e) { 
		var button = $(e.relatedTarget);
		var row = button.parents("tr");
		var user = row.find(".user_input").text();
		var pass = row.find(".pass_input").text();
		var type = row.find(".type_input").text();
		console.log(button, row);
		$(this).find(".user_input").val(user);
		$(this).find(".pass_input").val(pass);
		$("#type_input").val(type);
		console.log(user, pass);
	});

	// Purpose: User clicks on delete button
	$(".delete_account_btn").on("click", function(){
		$("#confirm_delete_account").modal("show");
	});

	// Purpose: Confirmation screen to delete account information
	//$(".confirm_delete_btn").on("click", function(){
	//	$("#form_id").submit();
	//});


	// Purpose: User clicks on save button
	$(".edit_account_btn").on("click", function(){
		$("#confirm_edit_account").modal("show");
	});


	/*
	$('.test').on("click", function() {
		var username_input =  $(this).closest('tr').find(".user_input").text();
		alert(username_input);
		console.log(username_input);
		window.location.href = "/admin-editaccount-Facilitator-edit" +username_input;

		
		$.ajax({
			url: '/admin-editaccount-Facilitator',
			type: 'POST',

		});
		
	});
	*/


	// Purpose: Confirmation screen to save account information 
	//$(".confirm_edit_btn").on("click", function(){
	//	alert("hi");
	//});
});