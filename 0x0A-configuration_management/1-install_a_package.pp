# Install flask package from pip3 using Puppet

exec { 'install_python3_pip':
  command => '/usr/bin/apt-get update && /usr/bin/apt-get install -y python3-pip',
  unless  => '/usr/bin/dpkg -l | grep -q "python3-pip"',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Exec['install_python3_pip'],
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.0.2',
  unless  => '/usr/bin/pip3 show Werkzeug | grep -q "Version: 2.0.2"',
  require => Exec['install_flask'],
}
