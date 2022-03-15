<?php 

$command = escapeshellcmd('./facial_recognition.py');
$output = shell_exec($command);
print $output;

?>
