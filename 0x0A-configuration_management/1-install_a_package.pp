# install flask from pip3
exec { 'Flask':
  command  => 'apt install flask',
  ensure   => '2.1.0',
  provider => 'pip3',
}
