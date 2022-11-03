# configuration file for servers

exec {'update':
  command  => 'sudo apt-get -y update',
  provider => 'shell',
  before   => package['restart']
}

package {'nginx':
  ensure => 'installed',
  before => Exec['serverHeader']
}

$host = $hostname

exec {'serverHeader':
  command  => "sudo sed -e '52i \\\t\tadd_header X-Served-By ${host};' -i /etc/nginx/sites-available/default;"
  provider => 'shell',
  before   => Exec['restart']
}

exec {'restart':
  user     => root,
  command  => 'sudo service nginx restart',
  provider => 'shell'
}
