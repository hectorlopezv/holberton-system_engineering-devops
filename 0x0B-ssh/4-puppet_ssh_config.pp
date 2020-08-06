#installing package to install puppet lint on agents

file {'ssh_config':
  ensure  => 'file',
  content => '
    Host * 
    IdentityFile ~/.ssh/holberton
    PasswordAuthentication no',
    path    => '/etc/ssh/ssh_config',
}
