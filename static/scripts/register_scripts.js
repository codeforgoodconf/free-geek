/**
 * Created by emanuel on 7/31/17.
 */

function checkBothPasswords() {
    //This function serves two purposes.
    //The first is to verify that the password falls within certain parameters
    var pWordOne = document.getElementById('password').value;
    var pWordTwo = document.getElementById('password_check').value;

    document.getElementById('register_button').disabled = false;
    document.getElementById('password_error').innerHTML='';
    if (pWordOne !== pWordTwo) {
	document.getElementById('register_button').disabled = true;
	document.getElementById('password_error').innerHTML += 'Passwords must be equal.<br>';
    }
    if (pWordOne.length < 5) {
	document.getElementById('register_button').disabled = true;
	document.getElementById('password_error').innerHTML +=('Password must be at least 5 characters.<br>');
    }

}