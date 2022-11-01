# nginx configuration

exec {'update':
  command  => 'sudo apt-get -y update',
  provider => 'shell'
}

package {'nginx':
  ensure => 'installed'
}

file {'index.html':
  path    => '/var/www/html/index.html'
  owner   => 'root',
  content => 'Hello World!\n'
}

$rdr_str = "\\\trewrite ^/redirect_me https://github.com/ExtranoDev permanent;"

exec {'rdr_str':
  user     => 'root',
  command  => "sed -i '51i ${rdr_str}' /etc/nginx/sites-available/default",
  provider => 'shell'
}

exec {'nginx_restart':
  user     => root,
  command  => 'service nginx start',
  provider => 'shell'
}
