# Create manifest that kills process

exec { 'pkill':
  command => 'pkill -f killmenow'
}
