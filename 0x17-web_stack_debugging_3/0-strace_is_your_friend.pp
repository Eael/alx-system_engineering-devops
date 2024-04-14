#Automate fixing config script in apache2 server


exec { 'Fix typo':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => 'shell',
}
