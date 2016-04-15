<?php
	$check = "/websites/secure/www/status.txt";
	$fh = fopen($check, "r");
	$l = fread($fh, filesize($check));
	$key = $_POST['key'];


	if (strcmp($l, $key) == 0)
	{
		$file = '/images/'. $_POST['picture'];
		if ($_POST['type'] == 0)
		{
			$imgbinary = fread(fopen($file, "r"), filesize($file));

			$img_str = base64_encode($imgbinary);

			echo $img_str;
		}
		else
		{
			$source_image = imagecreatefromjpeg($file);
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
	else{
		echo $key ;
		echo "     ";
		echo $l;
	}
?>
