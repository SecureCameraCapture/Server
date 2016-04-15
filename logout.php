<?php
	$key = $_POST['key'];
	$fh = fopen("status.txt", 'r');
	$k = fread($fh, filesize("status.txt"));
	if(strcmp($k, $key) == 0){
		unlink('status.txt');
		echo '0';
	}
	else
		echo '1';
?>
