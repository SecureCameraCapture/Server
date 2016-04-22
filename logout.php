<?php
	$key = $_POST['key'];
	$fh = fopen("status.txt", 'r');
	$l = fread($fh, filesize("status.txt"));
	$k = split(",", $l);
	fclose($fh);
	$fh2 = fopen("status.txt", 'w+');

	foreach($k as $value)
	{
		if(strcmp($value, $key) == 0){
		}
		else{
			if(!empty($value))
			{
				fwrite($fh2, ($value .","));
			}
		}
	}
	echo 0;
?>
