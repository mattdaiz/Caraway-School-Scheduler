// JavaScript source code
$( document ).ready(function() {
	$("#accountInfo").on("show.bs.modal", function (e) { 
		var button = $(e.relatedTarget);
		var row = button.parents("tr");
		var id = row.find(".id_input").text();
		var username = row.find(".user_input").text();
		var first = row.find(".first_input").text();
		var last = row.find(".last_input").text();
		var type = row.find(".type_input").text();
		$(this).find(".id_input").val(id);
		$(this).find(".user_input").val(username);
		$(this).find(".first_input").val(first);
		$(this).find(".last_input").val(last);
		$("#type_input").val(type);
	});

	// Purpose: User clicks on delete button
	$(".delete_account_btn").on("click", function(){
		$("#confirm_delete_account").modal("show");
	});

	// Purpose: User clicks on save button
	$(".edit_account_btn").on("click", function(){
		$("#confirm_edit_account").modal("show");
	});

	// Purpose: User clicks on save button
	$(".save_account_btn").on("click", function(){
		$("#confirm_save_account").modal("show");
	});


});