	  var intervalID;

	  function stopDO(){
		//console.log("stopDO intervalID is "   + intervalID);
		  if (intervalID) clearInterval(intervalID);  
	  	}
	  
// Search contact function
 function search(urlStr) {
 	 
	 	//console.log("demoTimeSelect is: " + urlStr);
	 	var request = $.ajax({
	 		type: 'POST',
	 		timeout: 30000,
	 		url: path + "/getdemos.action",
	 		data: {demoTimeSelect: urlStr}

	 	}); // End of AJAX post


	 	// done function
	 	request.done(function(msg) {
	 		$("#demoOptGroup").html(msg.demoTimeOptions);
	 	});  // end done function
	 
} // End contact search function


//CHECK SESSION SUBMIT
function check_session() {
	 var sessionDeferred = $.Deferred();
	 var sessionPromise = $.ajax({
		type: 'POST',
		timeout: 30000,
		url: path + "/checkSession.action",
	});

	 sessionPromise.then(
			 
		 function(msg) {
			//console.log("@ 1279 rpm2013_script checkSessionPromise doneCallBack ");
			if (msg.timeOut != null ) {
				_TITLE = msg.title;
				_MSG = msg.timeOut;
				
				//console.log("@1284 rpm2013_script reject deferred due to timeout msg.timeOut is: " + msg.timeOut);
				sessionDeferred.reject();

				$('div#completeDiv').html('').append('<p><span class="ui-icon ui-icon-alert" style="float: left; margin: 0 7px 20px 0;"></span>' + _MSG + '</p>').dialog({
					height: 140, 
					modal: true, 
					title: _TITLE,
					close: function( event , ui ) {
			 			window.location = path + "/start.action";
					},
					buttons: {
						Ok: function() {
							$( this).dialog( "close" );
						}
					}
				}) ;
	 			
				
			} else {
					
					//console.log("@1307 Resolve deferred, session active");
					sessionDeferred.resolve();
				}

			
	 } , 
	 
	 	function(msg) {
			//console.log("@ 1317 rpm2013_script checkSessionPromise failCallBack, reject deferred ");
			sessionDeferred.reject();
			
			if (msg.errMsg != null ) {
				//console.log("onsite_script ajax_submit errMsg returned");
				$('div#errContainer').html('').append('<ul><li>' + msg.errMsg + '</li></ul>') ;
				$('div#errContainer').slideDown(500);
				//_VALIDSESSION = false;
			} else {
				//console.log("onsite_script ajax_submit errMsg Not returned to fail method");
				$('div#errContainer').html('').append('<ul><li>System failure</li></ul>') ;
				$('div#errContainer').slideDown(500);
				//_VALIDSESSION = false;
			}

	 });
	 
	 return sessionDeferred.promise();
}
// END CHECK SESSION SUBMIT


