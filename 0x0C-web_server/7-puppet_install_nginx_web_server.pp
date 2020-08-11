
#hpow to use install nginx and start service and some file
package 
{
  'nginx':
  ensure  => 'installed',
}

service
{ 'nginx':
  ensure  => running,
  require => Package["nginx"],
}


file_line { 'sudo_rule':
  ensure  => 'present',
  path => '/etc/nginx/sites-available/default',
  after => 'listen [::]:80 default_server;',
  line => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file {
  'index.html':
  ensure  => 'file',
  path => '/var/www/html/',
  content => 'Holberton School',
}
