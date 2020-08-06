# creates a manifest for holberton file for server X
file {
  'holberton':
  ensure => 'file',
  path => '/tmp/holberton',
  owner => 'www-data',
  group => 'www-data',
  content => 'I love Puppet',
  mode => '0744',
}
