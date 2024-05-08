#!/usr/bin/env bash
# makes changes to config file using Puppet

include stdlib

file_line { 'PermitRootLogin':
  ensure => 'present',
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/sshd_config',
}

file_line { 'Use private key':
  ensure => 'present',
  line   => 'IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/sshd_config',
}