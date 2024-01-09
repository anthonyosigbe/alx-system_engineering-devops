# Install Nginx web server with Puppet
#
# Requirements:
# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request
# (requesting a page) using curl, it must return
# a page that contains the string Hello World!

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/anthonyosigbe permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
