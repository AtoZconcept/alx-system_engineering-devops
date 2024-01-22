# puppet file to to change ssh/config file
file { '/root/.ssh/config':
  ensure => present,
  mode   => '0600',
  content => "\
  Host advanced-task
    Hostname 54.146.79.250
	User ubuntu
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
",
}