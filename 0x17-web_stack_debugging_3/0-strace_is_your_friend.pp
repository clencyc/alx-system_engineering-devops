#  check why apache returns 500 error and fix it

file { '/var/www/html/wp-settings.php':
    ensure => present,
    owner => 'www-data',
    group => 'www-data',
    mode => '0644',
}

exec {
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path            => '/usr/local/bin/:/bin/'
}