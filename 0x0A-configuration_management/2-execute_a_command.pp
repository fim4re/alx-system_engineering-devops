# kill killmenow
exec { 'pkill':
  command  => 'pkill killmenow',
  path => '/bin/',
}
