#!/usr/bin/env ruby
# Match "hbtn, hbttn, hbtttn, hbttttn, hbtttttn"

puts ARGV[0].scan(/hbt{2,5}n/).join
