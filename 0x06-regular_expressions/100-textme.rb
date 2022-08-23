#!/usr/bin/env ruby
puts ARGV[0].scan(/from:([A-Za-z0-9+]+)\]\s\[to:([0-9+]+)\]\s\[flags:([0-9\-:]+)/).join(",")
