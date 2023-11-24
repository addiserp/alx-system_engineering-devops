# Using Puppet, install flask from pip3.

exec { 'install flask v2.1.0':
  ensure  => '2.1.0',
  command => '/usr/bin/pip3 install flask',
}
