# Puppet manifest to kill a process named "killmenow"

exec { 'kill_process':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
