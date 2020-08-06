#stop process but better use BOLT
exec { 'killmenow':
command  => 'pkill killmenow',
provider => 'shell',
path     => '/usr/bin',
}
