#!/usr/bin/env bash
# Script to edit configuration file

include stdlib
file_line { 'Off required password':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '   PasswordAuthentication no',
  replace => 'true'
}

file_line { 'Use private key':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '   IdentityFile ~/.ssh/school',
  replace => 'true'
}
