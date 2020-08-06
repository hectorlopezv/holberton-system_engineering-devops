#using exe manifest to stop a running process

exec {
  'killmenow':
  command => 'pkill killmenow',
  user    => 'root',

}
