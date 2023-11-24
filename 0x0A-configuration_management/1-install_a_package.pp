# Using Puppet, install flask from pip3.
exec { 'puppet-lint':
  command => '/usr/bin/pip3 install flask==2.1.0'
}
