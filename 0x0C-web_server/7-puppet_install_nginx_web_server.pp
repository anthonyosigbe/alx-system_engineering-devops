# Install Nginx web server with Puppet
#
# Requirements:
# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request
# (requesting a page) using curl, it must return
# a page that contains the string Hello World!

include stdlib

$link = 'http://example.com/'
$content = "\trewrite ^/redirect_me/$ ${link} permanent;"

exec { 'update packages':
  command => '/usr/bin/apt-get update'
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update packages']
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World',
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
}

file_line { 'Set 301 redirection':
  ensure   => 'present',
  after    => 'server_name\ _;',
  path     => '/etc/nginx/sites-available/default',
  multiple => true,
  line     => $content,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.html']
}
