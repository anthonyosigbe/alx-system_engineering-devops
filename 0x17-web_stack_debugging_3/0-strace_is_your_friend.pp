# Corrects incorrect 'phpp' extensions to 'php' in 'wp-settings.php' for WordPress.

exec { 'correct-php-extension-in-wp-settings':
  command     => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path        => '/usr/bin:/bin:/usr/sbin:/sbin',
  onlyif      => "grep -q 'phpp' /var/www/html/wp-settings.php",
}
