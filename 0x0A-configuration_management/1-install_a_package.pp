# Install flask package from pip3 using Puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
