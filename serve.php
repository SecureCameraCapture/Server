<?php
	$check = "/websites/secure/www/status.txt";
	$fh = fopen($check, "r");
	$l = fread($fh, filesize($check));
	$key = $_POST['key'];
	$k = split(",", $l);
	$t = 0;
	foreach($k as $value)
	{
		if (strcmp($value, $key) == 0)
		{
			$t = 1;
			$file = '/images/'. $_POST['picture'];
			if ($_POST['type'] == 0)
			{
				exec("python encrypt.py " . $file . " temp.jpg");

				$imgbinary = fread(fopen("temp.jpg", "r"), filesize("temp.jpg"));

				$img_str = base64_encode($imgbinary);

				echo $img_str;
			}
			else
			{
				exec("python encrypt.ph " . $file ." temp.jpg");
				$source_image = imagecreatefromjpeg("temp.jpg");
				$width = imagesx($source_image);
				$height = imagesy($source_image);

				$dh = floor($height * (480 / $width));

				$vi = imagecreatetruecolor(480,$dh);

				imagecopyresampled($vi, $source_image, 0, 0, 0, 0, 480, $dh, $width, $height);
				ob_start();
				imagejpeg($vi);
				$img = ob_get_contents();
				ob_end_clean();
				$image_data_64 = base64_encode($img);
				echo $image_data_64;
			}
		}
	}
	if($t == 0)
	{
		echo -1;
	}
?>
