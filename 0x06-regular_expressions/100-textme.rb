#!/usr/bin/ruby
cmd_arg = ARGV[0]

sender = cmd_arg.scan(/from:(\+?[a-zA-Z]*\d*)/)
reciever = cmd_arg.scan(/to:(\+?\d+)/)
flags = cmd_arg.scan(/flags:(-?\d:-?\d:-?\d:-?\d:-?\d)/)


print "#{sender[0][0]},#{reciever[0][0]},#{flags[0][0]}\n"
