# puppet file to to change ssh/config file
file { '/root/.ssh/config':
  ensure  => present,
  mode    => '0600',
  content => '',
}

file_line { 'Turn off passwd auth':
  path  => '/root/.ssh/config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication.*$',
}

file_line { 'Declare identity file':
  path  => '/root/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile.*$',
}
