# Install Nginx web server with Puppet
package { 'nginx':
  ensure => installed,
}

file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.google.com permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}