<?php 

$command = escapeshellcmd('./goldratio.py');
$output = shell_exec($command);
print $output;

?>
